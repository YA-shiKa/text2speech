from TTS.api import TTS
import numpy as np
import io
import soundfile as sf
from pydub import AudioSegment
from langdetect import detect

tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False).to("cpu")
multilingual_speaker = "p315" if "p315" in tts.speakers else tts.speakers[0]

def generate_audio_stream(text: str):
    try:
        lang = detect(text)
        if lang not in ["en", "hi"]:
            lang = "en"
    except:
        lang = "en"

    try:
        wav = tts.tts(text=text, speaker=multilingual_speaker, language=lang)
        wav_io = io.BytesIO()
        sf.write(wav_io, wav, 22050, format="WAV")
        wav_io.seek(0)
        audio = AudioSegment.from_file(wav_io, format="wav")
        mp3_io = io.BytesIO()
        audio.export(mp3_io, format="mp3")
        mp3_io.seek(0)
        return mp3_io
    except Exception as e:
        print("❌ Failed to generate audio:", e)
        return None