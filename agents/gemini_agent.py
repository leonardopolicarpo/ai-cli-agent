from google.generativeai import GenerativeModel
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = GenerativeModel("gemini-2.5-flash-preview-04-17-thinking")

def generate_response_gemini(prompt: str) -> str:
  response = model.generate_content(prompt)
  return response.text.strip()
