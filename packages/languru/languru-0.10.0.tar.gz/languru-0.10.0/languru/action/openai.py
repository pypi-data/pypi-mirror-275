import os
from typing import TYPE_CHECKING, Generator, List, Literal, Optional, Text, Union

import openai

from languru.action.base import ActionBase, ModelDeploy
from languru.config import logger

if TYPE_CHECKING:
    from openai._types import FileTypes
    from openai.types import (
        Completion,
        CreateEmbeddingResponse,
        ImagesResponse,
        ModerationCreateResponse,
    )
    from openai.types.audio import Transcription, Translation
    from openai.types.chat import (
        ChatCompletion,
        ChatCompletionChunk,
        ChatCompletionMessageParam,
    )


class OpenaiAction(ActionBase):
    model_deploys = (
        ModelDeploy("babbage-002", "babbage-002"),
        ModelDeploy("dall-e-2", "dall-e-2"),
        ModelDeploy("dall-e-3", "dall-e-3"),
        ModelDeploy("davinci-002", "davinci-002"),
        ModelDeploy("gpt-3.5-turbo", "gpt-3.5-turbo"),
        ModelDeploy("gpt-3.5-turbo-0125", "gpt-3.5-turbo-0125"),
        ModelDeploy("gpt-3.5-turbo-0301", "gpt-3.5-turbo-0301"),
        ModelDeploy("gpt-3.5-turbo-0613", "gpt-3.5-turbo-0613"),
        ModelDeploy("gpt-3.5-turbo-1106", "gpt-3.5-turbo-1106"),
        ModelDeploy("gpt-3.5-turbo-16k", "gpt-3.5-turbo-16k"),
        ModelDeploy("gpt-3.5-turbo-16k-0613", "gpt-3.5-turbo-16k-0613"),
        ModelDeploy("gpt-3.5-turbo-instruct", "gpt-3.5-turbo-instruct"),
        ModelDeploy("gpt-3.5-turbo-instruct-0914", "gpt-3.5-turbo-instruct-0914"),
        ModelDeploy("gpt-4", "gpt-4"),
        ModelDeploy("gpt-4-0125-preview", "gpt-4-0125-preview"),
        ModelDeploy("gpt-4-0613", "gpt-4-0613"),
        ModelDeploy("gpt-4-1106-preview", "gpt-4-1106-preview"),
        ModelDeploy("gpt-4-turbo-preview", "gpt-4-turbo-preview"),
        ModelDeploy("gpt-4-vision-preview", "gpt-4-vision-preview"),
        ModelDeploy("text-embedding-3-large", "text-embedding-3-large"),
        ModelDeploy("text-embedding-3-small", "text-embedding-3-small"),
        ModelDeploy("text-embedding-ada-002", "text-embedding-ada-002"),
        ModelDeploy("text-moderation-latest", "text-moderation-latest"),
        ModelDeploy("text-moderation-stable", "text-moderation-stable"),
        ModelDeploy("tts-1", "tts-1"),
        ModelDeploy("tts-1-1106", "tts-1-1106"),
        ModelDeploy("tts-1-hd", "tts-1-hd"),
        ModelDeploy("tts-1-hd-1106", "tts-1-hd-1106"),
        ModelDeploy("whisper-1", "whisper-1"),
        ModelDeploy("openai/babbage-002", "babbage-002"),
        ModelDeploy("openai/dall-e-2", "dall-e-2"),
        ModelDeploy("openai/dall-e-3", "dall-e-3"),
        ModelDeploy("openai/davinci-002", "davinci-002"),
        ModelDeploy("openai/gpt-3.5-turbo", "gpt-3.5-turbo"),
        ModelDeploy("openai/gpt-3.5-turbo-0125", "gpt-3.5-turbo-0125"),
        ModelDeploy("openai/gpt-3.5-turbo-0301", "gpt-3.5-turbo-0301"),
        ModelDeploy("openai/gpt-3.5-turbo-0613", "gpt-3.5-turbo-0613"),
        ModelDeploy("openai/gpt-3.5-turbo-1106", "gpt-3.5-turbo-1106"),
        ModelDeploy("openai/gpt-3.5-turbo-16k", "gpt-3.5-turbo-16k"),
        ModelDeploy("openai/gpt-3.5-turbo-16k-0613", "gpt-3.5-turbo-16k-0613"),
        ModelDeploy("openai/gpt-3.5-turbo-instruct", "gpt-3.5-turbo-instruct"),
        ModelDeploy(
            "openai/gpt-3.5-turbo-instruct-0914", "gpt-3.5-turbo-instruct-0914"
        ),
        ModelDeploy("openai/gpt-4", "gpt-4"),
        ModelDeploy("openai/gpt-4-0125-preview", "gpt-4-0125-preview"),
        ModelDeploy("openai/gpt-4-0613", "gpt-4-0613"),
        ModelDeploy("openai/gpt-4-1106-preview", "gpt-4-1106-preview"),
        ModelDeploy("openai/gpt-4-turbo-preview", "gpt-4-turbo-preview"),
        ModelDeploy("openai/gpt-4-vision-preview", "gpt-4-vision-preview"),
        ModelDeploy("openai/text-embedding-3-large", "text-embedding-3-large"),
        ModelDeploy("openai/text-embedding-3-small", "text-embedding-3-small"),
        ModelDeploy("openai/text-embedding-ada-002", "text-embedding-ada-002"),
        ModelDeploy("openai/text-moderation-latest", "text-moderation-latest"),
        ModelDeploy("openai/text-moderation-stable", "text-moderation-stable"),
        ModelDeploy("openai/tts-1", "tts-1"),
        ModelDeploy("openai/tts-1-1106", "tts-1-1106"),
        ModelDeploy("openai/tts-1-hd", "tts-1-hd"),
        ModelDeploy("openai/tts-1-hd-1106", "tts-1-hd-1106"),
        ModelDeploy("openai/whisper-1", "whisper-1"),
    )

    def __init__(
        self,
        *args,
        api_key: Optional[Text] = None,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)

        self._client = openai.OpenAI(api_key=api_key)

    def name(self):
        return "openai_action"

    def health(self) -> bool:
        try:
            self._client.models.retrieve(model="gpt-3.5-turbo")
            return True
        except Exception as e:
            logger.error(f"OpenAI health check failed: {e}")
            return False

    def chat(
        self, messages: List["ChatCompletionMessageParam"], *args, model: Text, **kwargs
    ) -> "ChatCompletion":
        model = self.validate_model(model)
        if kwargs.get("frequency_penalty") == 0.0:
            kwargs.pop("frequency_penalty")
        chat_completion = self._client.chat.completions.create(
            messages=messages, model=model, **kwargs
        )
        return chat_completion

    def chat_stream(
        self, messages: List["ChatCompletionMessageParam"], *args, model: Text, **kwargs
    ) -> Generator["ChatCompletionChunk", None, None]:
        if "stream" in kwargs and not kwargs["stream"]:
            logger.warning(f"Chat stream should be True, but got: {kwargs['stream']}")
        model = self.validate_model(model)
        kwargs.pop("stream", None)
        if kwargs.get("frequency_penalty") == 0.0:
            kwargs.pop("frequency_penalty")
        chat_completion_stream = self._client.chat.completions.create(
            messages=messages, model=model, stream=True, **kwargs
        )
        for _chat in chat_completion_stream:
            yield _chat

    def text_completion(
        self, prompt: Text, *args, model: Text, **kwargs
    ) -> "Completion":
        model = self.validate_model(model)
        completion = self._client.completions.create(
            prompt=prompt, model=model, **kwargs
        )
        return completion

    def text_completion_stream(
        self, prompt: Text, *args, model: Text, **kwargs
    ) -> Generator["Completion", None, None]:
        if "stream" in kwargs and not kwargs["stream"]:
            logger.warning(
                f"Text completion stream should be True, but got: {kwargs['stream']}"
            )
        kwargs.pop("stream", None)
        model = self.validate_model(model)
        completion_stream = self._client.completions.create(
            prompt=prompt, model=model, stream=True, **kwargs
        )
        for _completion in completion_stream:
            yield _completion

    def embeddings(
        self, input: Union[Text, List[Text]], *args, model: Text, **kwargs
    ) -> "CreateEmbeddingResponse":
        model = self.validate_model(model)
        embeddings = self._client.embeddings.create(input=input, model=model, **kwargs)
        return embeddings

    def moderations(
        self, input: Text, *args, model: Text, **kwargs
    ) -> "ModerationCreateResponse":
        model = self.validate_model(model)
        moderation = self._client.moderations.create(input=input, model=model, **kwargs)
        return moderation

    def audio_speech(
        self,
        input: Text,
        *args,
        model: Text,
        voice: Literal["alloy", "echo", "fable", "onyx", "nova", "shimmer"],
        **kwargs,
    ) -> Generator[bytes, None, None]:
        with self._client.audio.speech.with_streaming_response.create(
            input=input, model=model, voice=voice, **kwargs
        ) as response:
            for data in response.iter_bytes():
                yield data

    def audio_transcriptions(
        self, file: "FileTypes", *args, model: Text, **kwargs
    ) -> "Transcription":
        return self._client.audio.transcriptions.create(
            file=file, model=model, **kwargs
        )

    def audio_translations(
        self, file: "FileTypes", *args, model: Text, **kwargs
    ) -> "Translation":
        return self._client.audio.translations.create(file=file, model=model, **kwargs)

    def images_generations(
        self, prompt: Text, *args, model: Text, **kwargs
    ) -> "ImagesResponse":
        return self._client.images.generate(prompt=prompt, model=model, **kwargs)

    def images_edits(
        self, image: "FileTypes", *args, model: Text, **kwargs
    ) -> "ImagesResponse":
        return self._client.images.edit(image=image, model=model, **kwargs)

    def images_variations(
        self, image: "FileTypes", *args, model: Text, **kwargs
    ) -> "ImagesResponse":
        return self._client.images.create_variation(image=image, model=model, **kwargs)


class AzureOpenaiAction(OpenaiAction):
    model_deploys = (
        ModelDeploy("azure/gpt-3.5-turbo", "gpt-35-turbo"),
        ModelDeploy("azure/gpt-3.5-turbo-16k", "gpt-35-turbo-16k"),
        ModelDeploy("azure/gpt-3.5-turbo-instruct", "gpt-35-turbo-instruct"),
        ModelDeploy("azure/gpt-35-turbo", "gpt-35-turbo"),
        ModelDeploy("azure/gpt-35-turbo-16k", "gpt-35-turbo-16k"),
        ModelDeploy("azure/gpt-35-turbo-instruct", "gpt-35-turbo-instruct"),
        ModelDeploy("azure/gpt-4", "gpt-4"),
        ModelDeploy("azure/gpt-4-32k", "gpt-4-32k"),
        ModelDeploy("azure/text-embedding-3-large", "text-embedding-3-large"),
        ModelDeploy("azure/text-embedding-3-small", "text-embedding-3-small"),
        ModelDeploy("azure/text-embedding-ada-002", "text-embedding-ada-002"),
        ModelDeploy("gpt-3.5-turbo", "gpt-35-turbo"),
        ModelDeploy("gpt-3.5-turbo-16k", "gpt-35-turbo-16k"),
        ModelDeploy("gpt-3.5-turbo-instruct", "gpt-35-turbo-instruct"),
        ModelDeploy("gpt-35-turbo", "gpt-35-turbo"),
        ModelDeploy("gpt-35-turbo-16k", "gpt-35-turbo-16k"),
        ModelDeploy("gpt-35-turbo-instruct", "gpt-35-turbo-instruct"),
        ModelDeploy("gpt-4", "gpt-4"),
        ModelDeploy("gpt-4-32k", "gpt-4-32k"),
        ModelDeploy("text-embedding-3-large", "text-embedding-3-large"),
        ModelDeploy("text-embedding-3-small", "text-embedding-3-small"),
        ModelDeploy("text-embedding-ada-002", "text-embedding-ada-002"),
    )

    def __init__(
        self,
        *args,
        api_key: Optional[Text] = None,
        api_version: Optional[Text] = None,
        azure_endpoint: Optional[Text] = None,
        **kwargs,
    ):
        self._model_deploys = self.model_deploys

        __params = {}
        if api_key is not None:
            __params["api_key"] = api_key
        if api_version is not None:
            __params["api_version"] = api_version
        elif os.getenv("AZURE_OPENAI_API_VERSION"):
            __params["api_version"] = os.getenv("AZURE_OPENAI_API_VERSION")
        else:
            __params["api_version"] = "2024-02-01"
        if azure_endpoint is not None:
            __params["azure_endpoint"] = azure_endpoint
        self._client = openai.AzureOpenAI(**__params)

    def name(self):
        return "azure_openai_action"

    def health(self) -> bool:
        try:
            self._client.models.retrieve(model="gpt-35-turbo")
            return True
        except Exception as e:
            logger.error(f"OpenAI health check failed: {e}")
            return False
