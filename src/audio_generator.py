import asyncio
import edge_tts
from typing import Optional

class AudioGenerator:
    def __init__(self, voice: str = "pt-BR-AntonioNeural", rate: str = "+0%"):
        self.voice = voice
        self.rate = rate

    async def generate_audio(self, text: str, output_path: str) -> None:
        """Generate audio from text using EdgeTTS."""
        communicate = edge_tts.Communicate(text, self.voice, rate=self.rate)
        await communicate.save(output_path)

    def generate_audio_sync(self, text: str, output_path: str) -> None:
        """Synchronous wrapper for generate_audio."""
        asyncio.run(self.generate_audio(text, output_path))

    async def list_voices(self, filter_lang: Optional[str] = "pt-BR") -> list:
        """List available voices for a specific language."""
        voices = await edge_tts.VoicesManager.create()
        if filter_lang:
            return voices.find(Locale=filter_lang)
        return voices.voices
