import subprocess

def speak_text(text: str):
  subprocess.run([
    "espeak",
    "-v", "pt+m1",     # f1–f5, m1–m7
    "-s", "100",       # velocidade da fala (padrão 175)
    "-p", "60",        # pitch (0–99)
    text
  ])
