import streamlit as st
import pandas as pd

# Título do aplicativo
st.title("Analise de Currículos")

# Exibir um texto na tela
st.write("Faça o upload de seus currículos em DOCX ou PDF")

# Botão de upload de arquivo
uploaded_file = st.file_uploader("Escolha um arquivo .zip", type=["zip"])

# Formulário para coletar preferências adicionais da análise
with st.form("resume_preferences"):
    anos_experiencia = st.number_input(
        "Anos de experiência",
        min_value=0,
        step=1,
        value=0,
        help="Informe quantos anos de experiência profissional você possui.",
    )
    tempo_minimo_experiencias = st.number_input(
        "Tempo Mínimo entre Experiências (meses)",
        min_value=0,
        step=1,
        value=0,
        help="Tempo mínimo desejado entre cada experiência profissional listada.",
    )
    possui_trabalho_voluntario = st.checkbox("Possui Trabalho Voluntario")
    preferencias_enviadas = st.form_submit_button("Aplicar Preferências")

if preferencias_enviadas:
    st.session_state["resume_preferences"] = {
        "anos_experiencia": anos_experiencia,
        "tempo_minimo_experiencias": tempo_minimo_experiencias,
        "possui_trabalho_voluntario": possui_trabalho_voluntario,
    }
    st.success(
        "Preferências salvas: {} anos de experiência, mínimo de {} meses entre experiências, {} trabalho voluntário.".format(
            anos_experiencia,
            tempo_minimo_experiencias,
            "com" if possui_trabalho_voluntario else "sem",
        )
    )
elif "resume_preferences" in st.session_state:
    st.info(
        "Preferências atuais: {} anos de experiência, mínimo de {} meses entre experiências, {} trabalho voluntário.".format(
            st.session_state["resume_preferences"]["anos_experiencia"],
            st.session_state["resume_preferences"]["tempo_minimo_experiencias"],
            "com" if st.session_state["resume_preferences"]["possui_trabalho_voluntario"] else "sem",
        )
    )

# Verificar se um arquivo foi carregado
if uploaded_file is not None:
    st.success(f"Arquivo '{uploaded_file.name}' carregado com sucesso!")

    # Criar um botão para fazer o download do arquivo carregado
    st.write("Clique no botão abaixo para baixar o resumo dos arquivos:")
    st.download_button(
        label="Baixar Resumo",
        data=uploaded_file.getvalue(),
        file_name=uploaded_file.name,
        mime="application/zip"
    )
