# Copyright (c) Microsoft. All rights reserved.

import asyncio
import logging
from dataclasses import dataclass

import numpy as np
import weaviate
from pydantic import ValidationError

from semantic_kernel.connectors.memory.weaviate.weaviate_settings import WeaviateSettings
from semantic_kernel.memory.memory_record import MemoryRecord
from semantic_kernel.memory.memory_store_base import MemoryStoreBase
from semantic_kernel.utils.experimental_decorator import experimental_class

logger: logging.Logger = logging.getLogger(__name__)

SCHEMA = {
    "class": "MemoryRecord",
    "description": "A document from semantic kernel.",
    "properties": [
        {
            "name": "key",
            "description": "The key of the record.",
            "dataType": ["string"],
        },
        {
            "name": "timestamp",
            "description": "The timestamp of the record.",
            "dataType": ["date"],
        },
        {
            "name": "isReference",
            "description": "Whether the record is a reference record.",
            "dataType": ["boolean"],
        },
        {
            "name": "externalSourceName",
            "description": "The name of the external source.",
            "dataType": ["string"],
        },
        {
            "name": "skId",
            "description": "A unique identifier for the record.",
            "dataType": ["string"],
        },
        {
            "name": "description",
            "description": "The description of the record.",
            "dataType": ["text"],
        },
        {
            "name": "text",
            "description": "The text of the record.",
            "dataType": ["text"],
        },
        {
            "name": "additionalMetadata",
            "description": "Optional custom metadata of the record.",
            "dataType": ["string"],
        },
    ],
}

ALL_PROPERTIES = [property["name"] for property in SCHEMA["properties"]]


@dataclass
class WeaviateConfig:
    use_embed: bool = False
    url: str = None
    api_key: str = None


@experimental_class
class WeaviateMemoryStore(MemoryStoreBase):
    class FieldMapper:
        """
        This inner class is responsible for mapping attribute names between
        the SK's memory record and weaviate's schema. It provides methods
        for converting between the two naming conventions.
        """

        SK_TO_WEAVIATE_MAPPING = {
            "_key": "key",
            "_timestamp": "timestamp",
            "_is_reference": "isReference",
            "_external_source_name": "externalSourceName",
            "_id": "skId",
            "_description": "description",
            "_text": "text",
            "_additional_metadata": "additionalMetadata",
            "_embedding": "vector",
        }

        WEAVIATE_TO_SK_MAPPING = {v: k for k, v in SK_TO_WEAVIATE_MAPPING.items()}

        @classmethod
        def sk_to_weaviate(cls, sk_dict):
            return {
                cls.SK_TO_WEAVIATE_MAPPING.get(k, k): v for k, v in sk_dict.items() if k in cls.SK_TO_WEAVIATE_MAPPING
            }

        @classmethod
        def weaviate_to_sk(cls, weaviate_dict):
            return {
                cls.WEAVIATE_TO_SK_MAPPING.get(k, k): v
                for k, v in weaviate_dict.items()
                if k in cls.WEAVIATE_TO_SK_MAPPING
            }

        @classmethod
        def remove_underscore_prefix(cls, sk_dict):
            """
            Used to initialize a MemoryRecord from a SK's dict of private attribute-values.
            """
            return {key.lstrip("_"): value for key, value in sk_dict.items()}

    def __init__(self, config: WeaviateConfig | None = None, env_file_path: str | None = None):
        """Initializes a new instance of the WeaviateMemoryStore

        Optional parameters:
        - env_file_path {str | None} -- Whether to use the environment settings (.env) file. Defaults to False.
        """

        # Initialize settings from environment variables or defaults defined in WeaviateSettings
        weaviate_settings = None
        try:
            weaviate_settings = WeaviateSettings.create(env_file_path=env_file_path)
        except ValidationError as e:
            logger.warning(f"Failed to load WeaviateSettings pydantic settings: {e}")

        # Override settings with provided config if available
        if config:
            self.settings = self.merge_settings(weaviate_settings, config)
        else:
            self.settings = weaviate_settings

        self.settings.validate_settings()
        self.client = self._initialize_client()

    def merge_settings(self, default_settings: WeaviateSettings, config: WeaviateConfig) -> WeaviateSettings:
        """
        Merges default settings with configuration provided through WeaviateConfig.

        This function allows for manual overriding of settings from the config parameter.
        """
        return WeaviateSettings(
            url=config.url or (str(default_settings.url) if default_settings and default_settings.url else None),
            api_key=config.api_key
            or (default_settings.api_key.get_secret_value() if default_settings and default_settings.api_key else None),
            use_embed=(
                config.use_embed
                if config.use_embed is not None
                else (default_settings.use_embed if default_settings and default_settings.use_embed else False)
            ),
        )

    def _initialize_client(self) -> weaviate.Client:
        """
        Initializes the Weaviate client based on the combined settings.
        """
        if self.settings.use_embed:
            return weaviate.Client(embedded_options=weaviate.EmbeddedOptions())

        if self.settings.api_key:
            return weaviate.Client(
                url=self.settings.url, auth_client_secret=weaviate.auth.AuthApiKey(api_key=self.settings.api_key)
            )

        return weaviate.Client(url=self.settings.url)

    async def create_collection(self, collection_name: str) -> None:
        schema = SCHEMA.copy()
        schema["class"] = collection_name
        await asyncio.get_running_loop().run_in_executor(None, self.client.schema.create_class, schema)

    async def get_collections(self) -> list[str]:
        schemas = await asyncio.get_running_loop().run_in_executor(None, self.client.schema.get)
        return [schema["class"] for schema in schemas["classes"]]

    async def delete_collection(self, collection_name: str) -> bool:
        await asyncio.get_running_loop().run_in_executor(None, self.client.schema.delete_class, collection_name)

    async def does_collection_exist(self, collection_name: str) -> bool:
        collections = await self.get_collections()
        return collection_name in collections

    async def upsert(self, collection_name: str, record: MemoryRecord) -> str:
        weaviate_record = self.FieldMapper.sk_to_weaviate(vars(record))

        vector = weaviate_record.pop("vector", None)
        weaviate_id = weaviate.util.generate_uuid5(weaviate_record, collection_name)

        return await asyncio.get_running_loop().run_in_executor(
            None,
            self.client.data_object.create,
            weaviate_record,
            collection_name,
            weaviate_id,
            vector,
        )

    async def upsert_batch(self, collection_name: str, records: list[MemoryRecord]) -> list[str]:
        def _upsert_batch_inner():
            results = []
            with self.client.batch as batch:
                for record in records:
                    weaviate_record = self.FieldMapper.sk_to_weaviate(vars(record))
                    vector = weaviate_record.pop("vector", None)
                    weaviate_id = weaviate.util.generate_uuid5(weaviate_record, collection_name)
                    batch.add_data_object(
                        data_object=weaviate_record,
                        uuid=weaviate_id,
                        vector=vector,
                        class_name=collection_name,
                    )
                    results.append(weaviate_id)

            return results

        return await asyncio.get_running_loop().run_in_executor(None, _upsert_batch_inner)

    async def get(self, collection_name: str, key: str, with_embedding: bool) -> MemoryRecord:
        # Call the batched version with a single key
        results = await self.get_batch(collection_name, [key], with_embedding)
        return results[0] if results else None

    async def get_batch(self, collection_name: str, keys: list[str], with_embedding: bool) -> list[MemoryRecord]:
        queries = self._build_multi_get_query(collection_name, keys, with_embedding)

        results = await asyncio.get_running_loop().run_in_executor(None, self.client.query.multi_get(queries).do)

        get_dict = results.get("data", {}).get("Get", {})

        memory_records = [
            self._convert_weaviate_doc_to_memory_record(doc) for docs in get_dict.values() for doc in docs
        ]

        return memory_records

    def _build_multi_get_query(self, collection_name: str, keys: list[str], with_embedding: bool):
        queries = []
        for i, key in enumerate(keys):
            query = self.client.query.get(collection_name, ALL_PROPERTIES).with_where(
                {
                    "path": ["key"],
                    "operator": "Equal",
                    "valueString": key,
                }
            )
            if with_embedding:
                query = query.with_additional("vector")

            query = query.with_alias(f"query_{i}")

            queries.append(query)

        return queries

    def _convert_weaviate_doc_to_memory_record(self, weaviate_doc: dict) -> MemoryRecord:
        weaviate_doc_copy = weaviate_doc.copy()
        vector = weaviate_doc_copy.pop("_additional", {}).get("vector")
        weaviate_doc_copy["vector"] = np.array(vector) if vector else None
        sk_doc = self.FieldMapper.weaviate_to_sk(weaviate_doc_copy)
        mem_vals = self.FieldMapper.remove_underscore_prefix(sk_doc)
        return MemoryRecord(**mem_vals)

    async def remove(self, collection_name: str, key: str) -> None:
        await self.remove_batch(collection_name, [key])

    async def remove_batch(self, collection_name: str, keys: list[str]) -> None:
        # TODO: Use In operator when it's available
        #       (https://github.com/weaviate/weaviate/issues/2387)
        #       and handle max delete objects
        #       (https://weaviate.io/developers/weaviate/api/rest/batch#maximum-number-of-deletes-per-query)
        for key in keys:
            where = {
                "path": ["key"],
                "operator": "Equal",
                "valueString": key,
            }

            await asyncio.get_running_loop().run_in_executor(
                None, self.client.batch.delete_objects, collection_name, where
            )

    async def get_nearest_matches(
        self,
        collection_name: str,
        embedding: np.ndarray,
        limit: int,
        min_relevance_score: float,
        with_embeddings: bool,
    ) -> list[tuple[MemoryRecord, float]]:
        nearVector = {
            "vector": embedding,
            "certainty": min_relevance_score,
        }

        additional = ["certainty"]
        if with_embeddings:
            additional.append("vector")

        query = (
            self.client.query.get(collection_name, ALL_PROPERTIES)
            .with_near_vector(nearVector)
            .with_additional(additional)
            .with_limit(limit)
        )

        results = await asyncio.get_running_loop().run_in_executor(None, query.do)

        get_dict = results.get("data", {}).get("Get", {})

        memory_records_and_scores = [
            (
                self._convert_weaviate_doc_to_memory_record(doc),
                item["_additional"]["certainty"],
            )
            for items in get_dict.values()
            for item in items
            for doc in [item]
        ]

        return memory_records_and_scores

    async def get_nearest_match(
        self,
        collection_name: str,
        embedding: np.ndarray,
        min_relevance_score: float,
        with_embedding: bool,
    ) -> tuple[MemoryRecord, float]:
        results = await self.get_nearest_matches(
            collection_name,
            embedding,
            limit=1,
            min_relevance_score=min_relevance_score,
            with_embeddings=with_embedding,
        )

        return results[0]
