from pipeline import DocumentProcessor
import os

# Definir o caminho do arquivo PDF
PDF_FILE_PATH = "data/importancia_da_ia_no_setor_da_saude.pdf"

if __name__ == "__main__":
    processor = DocumentProcessor()
    
    print("🚀 Iniciando processamento do documento...")
    blog_post = processor.process_document(PDF_FILE_PATH)

    if blog_post:
        # Criar a pasta outputs/ se não existir
        os.makedirs("outputs", exist_ok=True)
        
        # Salvar o resultado
        output_file = "outputs/post_blog_exemplo1.md"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(blog_post)
        
        print(f"✅ Blog post salvo em {output_file}")
