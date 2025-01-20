import streamlit as st
import subprocess

# Inicializa a variável de sessão
if "first_run" not in st.session_state:
    st.session_state.first_run = True

st.title("🎈 My new app")
inputext = st.text_input('Digite o produto:', placeholder='Ex. Leite integral...')

if st.button('Pesquisar'):
    with st.spinner('Pesquisando...'):
        # Define o argumento com base na primeira execução
        select_city = st.session_state.first_run
        subOS = subprocess.run(["python", "scrapData.py", inputext, str(select_city)])

        # Atualiza o estado para False após a primeira execução
        if st.session_state.first_run:
            st.session_state.first_run = False

        st.write(subOS)
#
