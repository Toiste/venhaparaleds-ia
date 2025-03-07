from langchain.chat_models import ChatOpenAI
from config import get_openai_api_key

class InfoExtractor:
    """Agente responsável por identificar as informações mais importantes do texto."""

    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5, openai_api_key=get_openai_api_key())

    def extract_key_info(self, text):
        prompt = f"Extraia os principais pontos do seguinte texto:\n{text}"
        response = self.llm.predict(prompt)
        return response
