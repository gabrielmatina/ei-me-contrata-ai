import os
from pathlib import Path
from PyPDF2 import PdfReader

DOCS_DIR = Path("docs")

def delete_all_files():
    """ Remove todos os arquivos da pasta 'docs' """
    for file in DOCS_DIR.glob("*.pdf"):
        os.remove(file)

def read_pdf(file_path: str):
    """ Lê o conteúdo de um PDF e apaga o arquivo após a leitura """
    try:
        # Certifica-se de que a pasta existe
        DOCS_DIR.mkdir(parents=True, exist_ok=True)

        pdf_reader = PdfReader(file_path)
        text = "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
        
        # Apaga todos os arquivos após a leitura
        # delete_all_files()

        return text or "Não foi possível extrair texto do PDF."

    except Exception as e:
        return f"Erro ao ler o PDF: {str(e)}"
