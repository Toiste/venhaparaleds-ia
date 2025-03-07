from pypdf import PdfReader

class PDFReader:
    """Agente responsável por extrair o texto de um arquivo PDF."""

    def extract_text(self, file_path):
        try:
            reader = PdfReader(file_path)
            text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
            return text
        except Exception as e:
            print(f"Erro ao ler o PDF: {e}")
            return None
