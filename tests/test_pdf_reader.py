from src.agents.pdf_reader import PDFReader

def test_pdf_reader():
    reader = PDFReader()
    text = reader.extract_text("data/exemplo1.pdf")
    assert text is not None and len(text) > 0, "Erro ao extrair texto do PDF"
