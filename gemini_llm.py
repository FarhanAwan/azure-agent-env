import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class GeminiLLM:
    def complete(self, prompt: str) -> str:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)
        return response.text.strip()

llm = GeminiLLM()
response = llm.complete("How many Key Vaults do I have?")
print(response)

