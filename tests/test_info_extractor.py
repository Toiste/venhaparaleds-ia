from src.agents.info_extractor import InfoExtractor

def test_info_extractor():
    extractor = InfoExtractor()
    text = "Este é um documento de teste com informações importantes."
    key_info = extractor.extract_key_info(text)
    assert key_info is not None and len(key_info) > 0, "Erro ao extrair informações importantes"
