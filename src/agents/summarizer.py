from langchain.chat_models import ChatOpenAI
from config import get_openai_api_key

class Summarizer:
    """Agente que gera resumos concisos do conteúdo extraído."""

    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5, openai_api_key=get_openai_api_key())

    def summarize(self, text):
        prompt = f"Resuma o seguinte texto de maneira clara e objetiva:\n{text}"
        response = self.llm.predict(prompt)
        return response
