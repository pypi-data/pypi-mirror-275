import io
import tempfile
from typing import Any

import openai
from pydub import AudioSegment


class VoiceTranscription:
    def __init__(self, openai_key: str, logger: Any):
        self.openai_key = openai_key
        self.logger = logger

    async def get_voice_wav(self, client, event):
        voice_oga = await client.download_media(event.media, file=bytes)
        audio = AudioSegment.from_ogg(io.BytesIO(voice_oga))
        wav_io = io.BytesIO()
        audio.export(wav_io, format='wav')
        wav_io.seek(0)
        with tempfile.NamedTemporaryFile(suffix='.wav',
                                         delete=False) as temp_file:
            temp_file.write(wav_io.read())
        wav_io.close()
        msg = 'Got the voice file.'
        self.logger.get_voice_wav('info', msg)
        return temp_file.name

    async def get_text_transcription(self, audio_wav):
        openai.api_key = self.openai_key
        with open(audio_wav, 'rb') as audio_file:
            response = await openai.Audio.atranscribe('whisper-1', audio_file)
        msg = 'Transcript audio to text'
        self.logger.get_text_transcription('info', msg)
        return response.get('text')
