from TTS.api import TTS
import numpy as np
import io
import soundfile as sf
from pydub import AudioSegment

tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False).to("cpu")

available_speakers = tts.speakers
default_speaker = available_speakers[0]  

def generate_audio_stream(text: str):
    wav = tts.tts(text=text, speaker=default_speaker, language="en")

    wav_io = io.BytesIO()
    sf.write(wav_io, wav, 22050, format="WAV")
    wav_io.seek(0)

    audio = AudioSegment.from_file(wav_io, format="wav")
    mp3_io = io.BytesIO()
    audio.export(mp3_io, format="mp3")
    mp3_io.seek(0)
    return mp3_io
