from agents.pdf_reader import PDFReader
from agents.info_extractor import InfoExtractor
from agents.summarizer import Summarizer
from agents.blog_formatter import BlogFormatter

class DocumentProcessor:
    """Gerencia o fluxo de trabalho dos agentes."""

    def __init__(self):
        self.reader = PDFReader()
        self.extractor = InfoExtractor()
        self.summarizer = Summarizer()
        self.formatter = BlogFormatter()

    def process_document(self, file_path):
        print("🔹 Lendo PDF...")
        text = self.reader.extract_text(file_path)
        
        if not text:
            print("❌ Erro ao extrair texto do PDF.")
            return None
        
        print("🔹 Extraindo informações importantes...")
        key_info = self.extractor.extract_key_info(text)

        print("🔹 Gerando resumo...")
        summary = self.summarizer.summarize(key_info)

        print("🔹 Formatando como blog...")
        blog_post = self.formatter.format_as_blog(summary)

        return blog_post
