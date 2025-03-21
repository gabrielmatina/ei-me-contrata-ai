from decouple import config
from fastapi import FastAPI, File, UploadFile
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langserve import add_routes
from Test.chains import get_translate_chain
from fastapi import FastAPI, File, UploadFile
from pdf_processing import read_pdf, DOCS_DIR
from pathlib import Path
from profile_analysis import analyze_profile

model = ChatGroq(model_name="llama-3.3-70b-versatile", groq_api_key=config('GROQ_API_KEY'))

app = FastAPI(
    title="LinkedIn Analytics API",
    version="1.0",
    description="API para análise de perfis do LinkedIn"
)

add_routes(
    app,
    model,
    path='/chat'
    )

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """ Recebe um arquivo PDF do LinkedIn, processa e analisa o conteúdo """
    try:
        # Certifica-se de que a pasta existe
        DOCS_DIR.mkdir(parents=True, exist_ok=True)

        file_path = DOCS_DIR / file.filename

        # Salva o arquivo temporariamente
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        # Processa o PDF para extrair o texto
        extracted_text = read_pdf(file_path)

        # Envia para análise da IA
        analysis_result = analyze_profile(extracted_text)

        return {"message": "Arquivo processado com sucesso!", "analysis": analysis_result}

    except Exception as e:
        return {"error": f"Erro ao processar o arquivo: {str(e)}"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=8000)