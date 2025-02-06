# factory.py
from abc import ABC, abstractmethod
import openai
from transformers import pipeline

class LLMFactory(ABC):
    @abstractmethod
    def get_response(self, prompt: str) -> str:
        pass

class ChatGPT(LLMFactory):
    def __init__(self):
        openai.api_key = 'SUA API KEY'
        self.model = "gpt-4o-mini"

    def get_response(self, prompt: str) -> str:
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=100
            )
            return response['choices'][0]['message']['content'].strip()
        except Exception as e:
            return f"Erro ao acessar a API do ChatGPT: {e}"

class OtherLLM(LLMFactory):
    def __init__(self):
        self.generator = pipeline("text2text-generation", model="facebook/bart-large-cnn")

    def get_response(self, prompt: str) -> str:
        try:
            response = self.generator(prompt, max_length=50, num_return_sequences=1, truncation=True)
            return response[0]["generated_text"].strip()
        except Exception as e:
            return f"Erro ao gerar texto com o modelo da Hugging Face: {e}"