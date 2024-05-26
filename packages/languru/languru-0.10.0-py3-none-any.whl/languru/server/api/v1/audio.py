import logging
import math
import random
import time
from typing import Text, cast

from fastapi import (
    APIRouter,
    Body,
    Depends,
    File,
    Form,
    HTTPException,
    Request,
    UploadFile,
)
from fastapi.responses import StreamingResponse
from openai.types.audio import Transcription, Translation
from pyassorted.asyncio.executor import run_func, run_generator

from languru.exceptions import ModelNotFound
from languru.server.config import (
    AgentSettings,
    AppType,
    LlmSettings,
    ServerBaseSettings,
)
from languru.server.deps.common import app_settings
from languru.server.utils.common import get_value_from_app
from languru.types.audio import (
    AudioSpeechRequest,
    AudioTranscriptionRequest,
    AudioTranslationRequest,
)

router = APIRouter()


class AudioSpeechHandler:
    async def handle_request(
        self,
        request: "Request",
        audio_speech_request: "AudioSpeechRequest",
        settings: "ServerBaseSettings",
        **kwargs,
    ) -> StreamingResponse:
        if settings.APP_TYPE == AppType.llm:
            settings = cast(LlmSettings, settings)
            return await self.handle_llm(
                request=request,
                audio_speech_request=audio_speech_request,
                settings=settings,
                **kwargs,
            )

        if settings.APP_TYPE == AppType.agent:
            settings = cast(AgentSettings, settings)
            return await self.handle_agent(
                request=request,
                audio_speech_request=audio_speech_request,
                settings=settings,
                **kwargs,
            )

        # Not implemented or unknown app server type
        raise HTTPException(
            status_code=500,
            detail=(
                f"Unknown app server type: {settings.APP_TYPE}"
                if settings.APP_TYPE
                else "App server type not implemented"
            ),
        )

    async def handle_llm(
        self,
        request: "Request",
        audio_speech_request: "AudioSpeechRequest",
        settings: "LlmSettings",
        **kwargs,
    ) -> StreamingResponse:
        from languru.action.base import ActionBase

        action: "ActionBase" = get_value_from_app(
            request.app, key="action", value_typing=ActionBase
        )

        try:
            audio_speech_request.model = action.get_model_name(
                audio_speech_request.model
            )
        except ModelNotFound as e:
            raise HTTPException(status_code=404, detail=str(e))

        return StreamingResponse(
            run_generator(
                action.audio_speech,
                **audio_speech_request.model_dump(exclude_none=True),
            ),
            media_type="audio/mpeg",
        )

    async def handle_agent(
        self,
        request: "Request",
        audio_speech_request: "AudioSpeechRequest",
        settings: "AgentSettings",
        **kwargs,
    ) -> StreamingResponse:
        from openai import OpenAI

        from languru.resources.model_discovery.base import ModelDiscovery

        model_discovery: "ModelDiscovery" = get_value_from_app(
            request.app, key="model_discovery", value_typing=ModelDiscovery
        )
        logger = logging.getLogger(settings.APP_NAME)

        # Get model name and model destination
        models = await run_func(
            model_discovery.list,
            id=audio_speech_request.model,
            created_from=math.floor(time.time() - settings.MODEL_REGISTER_PERIOD),
        )
        if len(models) == 0:
            raise HTTPException(
                status_code=404,
                detail=f"Model '{audio_speech_request.model}' not found",
            )
        model = random.choice(models)

        # Request audio speech
        client = OpenAI(base_url=model.owned_by, api_key="NOT_IMPLEMENTED")
        logger.debug(f"Using model '{model.id}' from '{model.owned_by}'")
        with client.audio.speech.with_streaming_response.create(
            **audio_speech_request.model_dump(exclude_none=True)
        ) as response:
            return StreamingResponse(
                response.iter_bytes(),
                media_type="audio/mpeg",
            )


class AudioTranscriptionHandler:
    async def handle_request(
        self,
        request: "Request",
        audio_transcription_request: "AudioTranscriptionRequest",
        settings: "ServerBaseSettings",
        **kwargs,
    ) -> Transcription:
        if settings.APP_TYPE == AppType.llm:
            settings = cast(LlmSettings, settings)
            return await self.handle_llm(
                request=request,
                audio_transcription_request=audio_transcription_request,
                settings=settings,
                **kwargs,
            )

        if settings.APP_TYPE == AppType.agent:
            settings = cast(AgentSettings, settings)
            return await self.handle_agent(
                request=request,
                audio_transcription_request=audio_transcription_request,
                settings=settings,
                **kwargs,
            )

        # Not implemented or unknown app server type
        raise HTTPException(
            status_code=500,
            detail=(
                f"Unknown app server type: {settings.APP_TYPE}"
                if settings.APP_TYPE
                else "App server type not implemented"
            ),
        )

    async def handle_llm(
        self,
        request: "Request",
        audio_transcription_request: "AudioTranscriptionRequest",
        settings: "LlmSettings",
        **kwargs,
    ) -> Transcription:
        from languru.action.base import ActionBase

        action: "ActionBase" = get_value_from_app(
            request.app, key="action", value_typing=ActionBase
        )

        try:
            audio_transcription_request.model = action.get_model_name(
                audio_transcription_request.model
            )
        except ModelNotFound as e:
            raise HTTPException(status_code=404, detail=str(e))

        return await run_func(
            action.audio_transcriptions,
            **audio_transcription_request.model_dump(exclude_none=True),
        )

    async def handle_agent(
        self,
        request: "Request",
        audio_transcription_request: "AudioTranscriptionRequest",
        settings: "AgentSettings",
        **kwargs,
    ) -> Transcription:
        from openai import OpenAI

        from languru.resources.model_discovery.base import ModelDiscovery

        model_discovery: "ModelDiscovery" = get_value_from_app(
            request.app, key="model_discovery", value_typing=ModelDiscovery
        )
        logger = logging.getLogger(settings.APP_NAME)

        # Get model name and model destination
        models = await run_func(
            model_discovery.list,
            id=audio_transcription_request.model,
            created_from=math.floor(time.time() - settings.MODEL_REGISTER_PERIOD),
        )
        if len(models) == 0:
            raise HTTPException(
                status_code=404,
                detail=f"Model '{audio_transcription_request.model}' not found",
            )
        model = random.choice(models)

        # Request audio speech
        client = OpenAI(base_url=model.owned_by, api_key="NOT_IMPLEMENTED")
        logger.debug(f"Using model '{model.id}' from '{model.owned_by}'")
        return await run_func(
            client.audio.transcriptions.create,
            **audio_transcription_request.model_dump(exclude_none=True),
        )


class AudioTranslationHandler:
    async def handle_request(
        self,
        request: "Request",
        audio_translation_request: "AudioTranslationRequest",
        settings: "ServerBaseSettings",
        **kwargs,
    ) -> Translation:
        if settings.APP_TYPE == AppType.llm:
            settings = cast(LlmSettings, settings)
            return await self.handle_llm(
                request=request,
                audio_translation_request=audio_translation_request,
                settings=settings,
                **kwargs,
            )

        if settings.APP_TYPE == AppType.agent:
            settings = cast(AgentSettings, settings)
            return await self.handle_agent(
                request=request,
                audio_translation_request=audio_translation_request,
                settings=settings,
                **kwargs,
            )

        # Not implemented or unknown app server type
        raise HTTPException(
            status_code=500,
            detail=(
                f"Unknown app server type: {settings.APP_TYPE}"
                if settings.APP_TYPE
                else "App server type not implemented"
            ),
        )

    async def handle_llm(
        self,
        request: "Request",
        audio_translation_request: "AudioTranslationRequest",
        settings: "LlmSettings",
        **kwargs,
    ) -> Translation:
        from languru.action.base import ActionBase

        action: "ActionBase" = get_value_from_app(
            request.app, key="action", value_typing=ActionBase
        )

        try:
            audio_translation_request.model = action.get_model_name(
                audio_translation_request.model
            )
        except ModelNotFound as e:
            raise HTTPException(status_code=404, detail=str(e))

        return await run_func(
            action.audio_translations,
            **audio_translation_request.model_dump(exclude_none=True),
        )

    async def handle_agent(
        self,
        request: "Request",
        audio_translation_request: "AudioTranslationRequest",
        settings: "AgentSettings",
        **kwargs,
    ) -> Translation:
        from openai import OpenAI

        from languru.resources.model_discovery.base import ModelDiscovery

        model_discovery: "ModelDiscovery" = get_value_from_app(
            request.app, key="model_discovery", value_typing=ModelDiscovery
        )
        logger = logging.getLogger(settings.APP_NAME)

        # Get model name and model destination
        models = await run_func(
            model_discovery.list,
            id=audio_translation_request.model,
            created_from=math.floor(time.time() - settings.MODEL_REGISTER_PERIOD),
        )
        if len(models) == 0:
            raise HTTPException(
                status_code=404,
                detail=f"Model '{audio_translation_request.model}' not found",
            )
        model = random.choice(models)

        # Request audio speech
        client = OpenAI(base_url=model.owned_by, api_key="NOT_IMPLEMENTED")
        logger.debug(f"Using model '{model.id}' from '{model.owned_by}'")
        return await run_func(
            client.audio.translations.create,
            **audio_translation_request.model_dump(exclude_none=True),
        )


@router.post("/audio/speech")
async def audio_speech(
    request: Request,
    audio_speech_request: AudioSpeechRequest = Body(
        ...,
        openapi_examples={
            "OpenAI": {
                "summary": "OpenAI",
                "description": "Chat completion request",
                "value": {
                    "model": "tts-1",
                    "voice": "alloy",
                    "input": "The quick brown fox jumped over the lazy dog.",
                },
            },
        },
    ),
    settings: ServerBaseSettings = Depends(app_settings),
) -> StreamingResponse:
    return await AudioSpeechHandler().handle_request(
        request=request,
        audio_speech_request=audio_speech_request,
        settings=settings,
    )


@router.post("/audio/transcriptions")
async def audio_transcriptions(
    request: Request,
    file: UploadFile = File(...),
    model: Text = Form(...),
    language: Text = Form(None),
    prompt: Text = Form(None),
    response_format: Text = Form(None),
    temperature: float = Form(None),
    timestamp_granularities: Text = Form(None),
    timeout: float = Form(None),
    settings: ServerBaseSettings = Depends(app_settings),
) -> Transcription:
    return await AudioTranscriptionHandler().handle_request(
        request=request,
        audio_transcription_request=AudioTranscriptionRequest.model_validate(
            {
                "file": await file.read(),
                "model": model,
                "language": language,
                "prompt": prompt,
                "response_format": response_format,
                "temperature": temperature,
                "timestamp_granularities": timestamp_granularities,
                "timeout": timeout,
            }
        ),
        settings=settings,
    )


@router.post("/audio/translations")
async def audio_translations(
    request: Request,
    file: UploadFile = File(...),
    model: Text = Form(...),
    language: Text = Form(None),
    prompt: Text = Form(None),
    response_format: Text = Form(None),
    temperature: float = Form(None),
    timeout: float = Form(None),
    settings: ServerBaseSettings = Depends(app_settings),
) -> Translation:
    return await AudioTranslationHandler().handle_request(
        request=request,
        audio_translation_request=AudioTranslationRequest.model_validate(
            {
                "file": await file.read(),
                "model": model,
                "language": language,
                "prompt": prompt,
                "response_format": response_format,
                "temperature": temperature,
                "timeout": timeout,
            }
        ),
        settings=settings,
    )
