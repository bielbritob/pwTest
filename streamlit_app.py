import streamlit as st
import subprocess

# Inicializa a variável de sessão
if "first_run" not in st.session_state:
    st.session_state.first_run = True

st.title("🎈 My new app")
inputext = st.text_input('Digite o produto:', placeholder='Ex. Leite integral...')

if st.button('Pesquisar'):
    with st.spinner('Pesquisando...'):
        # Verifica se o usuário digitou o comando de instalação
        if inputext.strip().lower() == "pip install zendriver":
            st.write("Instalando ZenDriver...")
            result = subprocess.run(['pip', 'install', 'zendriver'], capture_output=True, text=True)
            if result.returncode == 0:
                st.success("ZenDriver instalado com sucesso!")
                st.write(result.stdout)
            else:
                st.error("Erro ao instalar ZenDriver:")
                st.write(result.stderr)
        else:
            # Define o argumento com base na primeira execução
            select_city = st.session_state.first_run
            subOS = subprocess.run(["python", "scrapData.py", inputext, str(select_city)], capture_output=True, text=True)

            # Atualiza o estado para False após a primeira execução
            if st.session_state.first_run:
                st.session_state.first_run = False

            st.write(subOS.stdout)
            if subOS.stderr:
                st.error(subOS.stderr)