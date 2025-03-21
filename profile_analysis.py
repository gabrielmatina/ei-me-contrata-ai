from decouple import config
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from prompts import (
    resumo_prompt,
    experiencias_prompt,
    habilidades_prompt,
    certificacoes_prompt,
    sugestoes_melhoria_prompt,
)

# Inicializa o modelo da IA
model = ChatGroq(model_name="llama-3.3-70b-versatile", groq_api_key=config("GROQ_API_KEY"))

def analyze_profile(extracted_text: str):
    """
    Analisa o perfil do LinkedIn com base no texto extraído do PDF.
    Retorna um dicionário com as respostas da IA para cada seção.
    """

    # Criar prompts individuais para cada seção do perfil
    prompts = {
        "resumo": resumo_prompt(extracted_text),
        "experiencia": experiencias_prompt(extracted_text),
        "habilidades": habilidades_prompt(extracted_text),
        "certificacoes": certificacoes_prompt(extracted_text),
        "sugestoes_melhoria": sugestoes_melhoria_prompt(extracted_text),
    }

    # Configurar a cadeia de análise da IA
    output_parser = StrOutputParser()
    results = {}

    for key, prompt_text in prompts.items():
        prompt = ChatPromptTemplate.from_template(prompt_text)
        chain = prompt | model | output_parser
        results[key] = chain.invoke({})

    return results
