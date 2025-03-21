# 🚀 Ei, Me Contrata AI  

## 📌 Sobre o Projeto  
**Ei, Me Contrata AI** é uma ferramenta que utiliza **Inteligência Artificial** para ajudar profissionais na busca por emprego. O projeto analisa o **perfil do LinkedIn** e o **currículo do usuário**, além de otimizar o currículo para uma vaga específica, aumentando suas chances no mercado de trabalho.  

## 🎯 Funcionalidades  
✅ **Análise do perfil do LinkedIn** – Avaliação do resumo, experiências e habilidades.  
✅ **Análise do currículo (PDF ou Word)** – Pontuação de aderência com base na área profissional.  
✅ **Otimização do currículo para uma vaga específica** – Personalização do documento conforme a descrição da vaga.  
✅ **Pontuação de aderência** – Comparação entre as palavras-chave do currículo e da vaga.  
✅ **Geração de carta de apresentação personalizada** – Baseada no currículo e LinkedIn.  
✅ **Sugestão de empresas e setores que mais contratam** – Utilizando APIs externas como Glassdoor e LinkedIn.  

## 🛠️ Tecnologias Utilizadas  
🚀 **Linguagem e Frameworks:**  
- Python  
- FastAPI  
- Streamlit  

🧠 **Inteligência Artificial e NLP:**  
- LangChain  
- Groq API (Llama 3.3 70B Versatile)  

📊 **Análise e Processamento de Dados:**  
- PyPDF2 (Leitura de PDFs)  
- ChromaDB (para busca vetorial, futuramente)  

🔗 **APIs Externas:**  
- Glassdoor API (Análise de mercado)  
- LinkedIn API (Sugestões para networking)  

## ⚙️ Como Rodar o Projeto  

### 🔧 **1. Clonar o repositório**  
```bash
git clone https://github.com/seu-usuario/ei-me-contrata-ai.git
cd ei-me-contrata-ai
```

### 🔧 **2. Criar um ambiente virtual e instalar dependências
```bash
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 🔧 **3. Rodar a API (FastAPI)
```bash
uvicorn app:app --reload
```

### 🔧 **4. Rodar a Interface Gráfica (Streamlit)
```bash
streamlit run app_streamlit.py
```

## 📌 **Roadmap do Projeto**
- ✅ Análise do LinkedIn
- ✅ Análise do Currículo
- ⏳ Otimização do currículo para uma vaga específica (Em desenvolvimento)
- ⏳ Pontuação de aderência (Em breve)
- ⏳ Geração de carta de apresentação (Em breve)
- ⏳ Integração com Glassdoor e LinkedIn API (Em breve)

## 📢 **Contribuições**
Se quiser contribuir com melhorias, fique à vontade para abrir issues e pull requests! 💡

