from cli.cli_session import select_session
from core.engine import run_agent
from audio.tts import speak_text
from audio.stt import transcribe_audio

def main():
  print("AI CLI Agent (CLI) - Digite 'sair' para encerrar.")
  session_id = select_session()
  print(f"Usando sessão: {session_id}")

  voice_mode = False  # modo de voz desativado por padrão

  while True:
    if voice_mode:
      print("\n🎤 Modo voz ativo. Fale algo ou digite /texto para voltar ao modo escrito.")
      prompt = transcribe_audio()  # STT: converte fala em texto
      if not prompt.strip():
        print("[⚠️ Nenhuma fala detectada.]")
        continue
      print(f"Você (voz): {prompt}")
    else:
      prompt = input("Você: ")
    
    if prompt.lower() in ["sair", "exit", "quit"]:
      break
    elif prompt.lower() == "voz":
      voice_mode = True
      print("[🔊 Modo voz ativado. Fale para interagir.]")
      speak_text("Modo voz ativado")
      continue
    elif prompt.lower() == "texto":
      voice_mode = False
      print("[📝 Modo texto reativado.]")
      continue

    # response = run_agent("gemini", prompt, session_id)
    response = "Testando isso aqui"

    if voice_mode:
      speak_text(response)
    else:
      print(f"Gemini: {response}\n")
