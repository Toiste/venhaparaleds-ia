from langchain.chat_models import ChatOpenAI
from config import get_openai_api_key

class BlogFormatter:
    """Agente responsável por formatar o resumo como um post de blog."""

    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7, openai_api_key=get_openai_api_key())

    def format_as_blog(self, summary):
        prompt = f"Formate este resumo como um post de blog bem estruturado, com título, subtítulos e conclusão:\n{summary}"
        response = self.llm.predict(prompt)
        return response
