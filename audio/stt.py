import whisper
import sounddevice as sd
import scipy.io.wavfile as wav
import tempfile

# "base" - precisão
# "small" | "medium" + precisão
model = whisper.load_model("medium")

def record_audio(duration=10, samplerate=16000):
  print(f"Gravando áudio por {duration} segundos...")
  audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
  sd.wait()
  return audio, samplerate

def transcribe_audio(duration=10):
  audio, samplerate = record_audio(duration)
  with tempfile.NamedTemporaryFile(suffix=".wav") as temp_wav:
    wav.write(temp_wav.name, samplerate, audio)
    result = model.transcribe(temp_wav.name, language="pt")
    return result["text"]
