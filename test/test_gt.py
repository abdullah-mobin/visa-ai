from gtts import gTTS
from pydub import AudioSegment
import simpleaudio as sa
import io

def speak(text, lang="en"):
    # Create in-memory bytes buffer
    mp3_fp = io.BytesIO()
    
    # Generate TTS to bytes
    tts = gTTS(text=text, lang=lang)
    tts.write_to_fp(mp3_fp)
    
    # Seek to start
    mp3_fp.seek(0)
    
    # Load mp3 data to AudioSegment
    audio = AudioSegment.from_file(mp3_fp, format="mp3")
    
    # Convert to raw audio data for playback
    raw_data = audio.raw_data
    sample_rate = audio.frame_rate
    channels = audio.channels
    sample_width = audio.sample_width
    
    # Play audio using simpleaudio
    play_obj = sa.play_buffer(raw_data, channels, sample_width, sample_rate)
    play_obj.wait_done()  # Wait until playback finishes

# Test it
speak("hi ,fuck you")
