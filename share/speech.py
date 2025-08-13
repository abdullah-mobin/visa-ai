
import asyncio
import edge_tts
import tempfile
import os
import subprocess

async def speak_edge(text: str):
    try:
        # Save the audio to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmpfile:
            temp_path = tmpfile.name

        communicate = edge_tts.Communicate(text, voice="en-US-JennyNeural")
        await communicate.save(temp_path)

        # Play the file using ffplay (safer than Python players)
        subprocess.run(["ffplay", "-nodisp", "-autoexit", temp_path],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        os.remove(temp_path)

    except Exception as e:
        print(f"❌ Edge TTS Error: {e}")
