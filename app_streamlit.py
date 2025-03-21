import streamlit as st
from pathlib import Path
from pdf_processing import read_pdf
from profile_analysis import analyze_profile

# Configuração da página
st.set_page_config(page_title="LinkedIn Profile Analyzer", layout="wide")

st.title("🔍 Analisador de Perfil do LinkedIn com IA")
st.write("Envie seu PDF do LinkedIn para obter uma análise completa do seu perfil!")

# Upload do arquivo
uploaded_file = st.file_uploader("Faça o upload do seu PDF exportado do LinkedIn", type=["pdf"])

if uploaded_file:
    # Caminho temporário para salvar o arquivo
    docs_dir = Path("docs")
    docs_dir.mkdir(exist_ok=True)  # Garante que a pasta existe
    file_path = docs_dir / "linkedin_profile.pdf"

    # Salva o arquivo temporariamente
    with open(file_path, "wb") as buffer:
        buffer.write(uploaded_file.getbuffer())

    st.success("✅ Arquivo carregado com sucesso!")

    # Exibir texto extraído
    st.subheader("📄 Texto extraído do PDF:")
    extracted_text = read_pdf(file_path)
    st.text_area("Conteúdo extraído:", extracted_text, height=300)

    # Botão para análise com IA
    if st.button("📊 Analisar Perfil"):
        with st.spinner("Analisando perfil com IA... ⏳"):
            analysis_result = analyze_profile(extracted_text)

        st.subheader("🧠 Resultados da Análise:")
        for key, result in analysis_result.items():
            st.markdown(f"### {key.capitalize()}")
            st.write(result)

    # Apaga o arquivo após o processamento
    # file_path.unlink()
