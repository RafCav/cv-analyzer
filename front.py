import streamlit as st
import pandas as pd

# Título do aplicativo
st.title("Analise de Currículos")

# Exibir um texto na tela
st.write("Faça o upload de seus currículos em DOCX ou PDF")

# Botão de upload de arquivo
uploaded_file = st.file_uploader("Escolha um arquivo .zip", type=["zip"])

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
