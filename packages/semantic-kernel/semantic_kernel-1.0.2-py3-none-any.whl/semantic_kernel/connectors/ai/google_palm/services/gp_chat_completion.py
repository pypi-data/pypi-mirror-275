# Copyright (c) Microsoft. All rights reserved.

import logging
from typing import Annotated, Any

import google.generativeai as palm
from google.generativeai.types import ChatResponse, MessageDict
from pydantic import PrivateAttr, StringConstraints, ValidationError

from semantic_kernel.connectors.ai.chat_completion_client_base import ChatCompletionClientBase
from semantic_kernel.connectors.ai.google_palm.gp_prompt_execution_settings import (
    GooglePalmChatPromptExecutionSettings,
    GooglePalmPromptExecutionSettings,
)
from semantic_kernel.connectors.ai.google_palm.settings.google_palm_settings import GooglePalmSettings
from semantic_kernel.connectors.ai.prompt_execution_settings import PromptExecutionSettings
from semantic_kernel.connectors.ai.text_completion_client_base import TextCompletionClientBase
from semantic_kernel.contents.author_role import AuthorRole
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.contents.chat_message_content import ChatMessageContent
from semantic_kernel.contents.text_content import TextContent
from semantic_kernel.exceptions import ServiceInvalidRequestError, ServiceResponseException

logger: logging.Logger = logging.getLogger(__name__)

int_to_role = {1: AuthorRole.USER, 2: AuthorRole.SYSTEM, 3: AuthorRole.ASSISTANT, 4: AuthorRole.TOOL}


class GooglePalmChatCompletion(ChatCompletionClientBase, TextCompletionClientBase):
    api_key: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    _message_history: ChatHistory | None = PrivateAttr()
    service_id: str | None = None

    def __init__(
        self,
        ai_model_id: str,
        api_key: str | None = None,
        message_history: ChatHistory | None = None,
        env_file_path: str | None = None,
    ):
        """
        Initializes a new instance of the GooglePalmChatCompletion class.

        Arguments:
            ai_model_id {str} -- GooglePalm model name, see
                https://developers.generativeai.google/models/language
            api_key {str | None} -- The optional API key to use. If not provided, will be read from either
                the env vars or the .env settings file
            message_history {ChatHistory | None} -- The message history to use for context. (Optional)
            env_file_path {str | None} -- Use the environment settings file as a fallback to
                environment variables. (Optional)
        """
        google_palm_settings = None
        try:
            google_palm_settings = GooglePalmSettings.create(env_file_path=env_file_path)
        except ValidationError as e:
            logger.warning(f"Error loading Google Palm pydantic settings: {e}")

        api_key = api_key or (
            google_palm_settings.api_key.get_secret_value()
            if google_palm_settings and google_palm_settings.api_key
            else None
        )
        ai_model_id = ai_model_id or (
            google_palm_settings.chat_model_id if google_palm_settings and google_palm_settings.chat_model_id else None
        )

        super().__init__(
            ai_model_id=ai_model_id,
            api_key=api_key,
        )
        self._message_history = message_history

    async def get_chat_message_contents(
        self,
        chat_history: ChatHistory,
        settings: GooglePalmPromptExecutionSettings,
        **kwargs: Any,
    ) -> list[ChatMessageContent]:
        """
        This is the method that is called from the kernel to get a response from a chat-optimized LLM.

        Arguments:
            chat_history {List[ChatMessage]} -- A list of chat messages, that can be rendered into a
                set of messages, from system, user, assistant and function.
            settings {GooglePalmPromptExecutionSettings} -- Settings for the request.
            kwargs {Dict[str, Any]} -- The optional arguments.

        Returns:
            List[ChatMessageContent] -- A list of ChatMessageContent objects representing the response(s) from the LLM.
        """
        settings.messages = self._prepare_chat_history_for_request(chat_history, role_key="author")
        if not settings.ai_model_id:
            settings.ai_model_id = self.ai_model_id
        response = await self._send_chat_request(settings)
        return [
            self._create_chat_message_content(response, candidate, index)
            for index, candidate in enumerate(response.candidates)
        ]

    def _create_chat_message_content(
        self, response: ChatResponse, candidate: MessageDict, index: int
    ) -> ChatMessageContent:
        """Create a chat message content object from a response.

        Arguments:
            response {ChatResponse} -- The response to create the content from.

        Returns:
            ChatMessageContent -- The created chat message content.
        """
        metadata = {
            "citation_metadata": candidate.get("citation_metadata"),
            "filters": response.filters,
            "choice_index": index,
        }
        return ChatMessageContent(
            inner_content=response,
            ai_model_id=self.ai_model_id,
            metadata=metadata,
            role=int_to_role[int(candidate.get("author"))],  # TODO: why is author coming back as '1'?
            content=candidate.get("content"),
        )

    async def get_streaming_chat_message_contents(
        self,
        messages: list[tuple[str, str]],
        settings: GooglePalmPromptExecutionSettings,
        **kwargs: Any,
    ):
        raise NotImplementedError("Google Palm API does not currently support streaming")

    async def get_text_contents(
        self,
        prompt: str,
        settings: GooglePalmPromptExecutionSettings,
    ) -> list[TextContent]:
        """
        This is the method that is called from the kernel to get a response from a text-optimized LLM.

        Arguments:
            prompt {str} -- The prompt to send to the LLM.
            settings {GooglePalmPromptExecutionSettings} -- Settings for the request.

        Returns:
            List[TextContent] -- A list of TextContent objects representing the response(s) from the LLM.
        """
        settings.messages = [{"author": "user", "content": prompt}]
        if not settings.ai_model_id:
            settings.ai_model_id = self.ai_model_id
        response = await self._send_chat_request(settings)

        return [self._create_text_content(response, candidate) for candidate in response.candidates]

    def _create_text_content(self, response: ChatResponse, candidate: MessageDict) -> TextContent:
        """Create a text content object from a response.

        Arguments:
            response {ChatResponse} -- The response to create the content from.

        Returns:
            TextContent -- The created text content.
        """
        metadata = {"citation_metadata": candidate.get("citation_metadata"), "filters": response.filters}
        return TextContent(
            inner_content=response,
            ai_model_id=self.ai_model_id,
            metadata=metadata,
            text=candidate.get("content"),
        )

    async def get_streaming_text_contents(
        self,
        prompt: str,
        settings: GooglePalmPromptExecutionSettings,
    ):
        raise NotImplementedError("Google Palm API does not currently support streaming")

    async def _send_chat_request(
        self,
        settings: GooglePalmPromptExecutionSettings,
    ):
        """
        Completes the given user message. If len(messages) > 1, and a
        conversation has not been initiated yet, it is assumed that chat history
        is needed for context. All messages preceding the last message will be
        utilized for context. This also enables Google PaLM to utilize memory
        and plugins, which should be stored in the messages parameter as system
        messages.

        Arguments:
            messages {str} -- The message (from a user) to respond to.
            settings {GooglePalmPromptExecutionSettings} -- The request settings.
            context {str} -- Text that should be provided to the model first,
            to ground the response. If a system message is provided, it will be
            used as context.
            examples {ExamplesOptions} -- 	Examples of what the model should
            generate. This includes both the user input and the response that
            the model should emulate. These examples are treated identically to
            conversation messages except that they take precedence over the
            history in messages: If the total input size exceeds the model's
            input_token_limit the input will be truncated. Items will be dropped
            from messages before examples
            See: https://developers.generativeai.google/api/python/google/generativeai/types/ExampleOptions
            prompt {MessagePromptOptions} -- 	You may pass a
            types.MessagePromptOptions instead of a setting context/examples/messages,
            but not both.
            See: https://developers.generativeai.google/api/python/google/generativeai/types/MessagePromptOptions

        Returns:
            str -- The completed text.
        """
        if settings is None:
            raise ValueError("The request settings cannot be `None`")

        if settings.messages[-1]["author"] != "user":
            raise ServiceInvalidRequestError("The last message must be from the user")
        try:
            palm.configure(api_key=self.api_key)
        except Exception as ex:
            raise PermissionError(
                "Google PaLM service failed to configure. Invalid API key provided.",
                ex,
            )
        try:
            if self._message_history is None:
                response = palm.chat(**settings.prepare_settings_dict())  # Start a new conversation
            else:
                response = self._message_history.reply(  # Continue the conversation
                    settings.messages[-1]["content"],
                )
            self._message_history = response  # Store response object for future use
        except Exception as ex:
            raise ServiceResponseException(
                "Google PaLM service failed to complete the prompt",
                ex,
            ) from ex
        return response

    def get_prompt_execution_settings_class(self) -> "PromptExecutionSettings":
        """Create a request settings object."""
        return GooglePalmChatPromptExecutionSettings
