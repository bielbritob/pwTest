import subprocess
import streamlit as st
import os



# Configuração da interface do Streamlit
st.set_page_config(page_title="PriceWise", page_icon="🛒", layout="centered")

# Título e barra de busca
st.title(" 🛒  PriceWise - Comparador de Preços")
product_name = st.text_input("Digite o produto que deseja pesquisar:",
                             placeholder="Ex. leite integral, cafe 500g (seja específico para melhor busca)")



# Iniciar busca
if st.button("Pesquisar"):
    with st.spinner("Pesquisando..."):
        nah = subprocess.run(['python', 'scrapData.py'], capture_output=True)
        st.write(f'output nah: {nah}')






if st.button('install deps'):
    os.system('pip install playwright')
    os.system('playwright install')
    os.system('playwright install-deps')