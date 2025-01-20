import streamlit as st
import subprocess

# Inicializa a variável de sessão
if "first_run" not in st.session_state:
    st.session_state.first_run = True

st.title("🎈 My new app")
inputext = st.text_input('Digite o produto:', placeholder='Ex. Leite integral...')

if st.button('Pesquisar'):
    with st.spinner('Pesquisando...'):
        # Verifica se o usuário digitou um comando de instalação
        if inputext.strip().lower().startswith("pip install"):
            package = inputext.strip().lower().replace("pip install", "").strip()
            if package in ["zendriver", "beautifulsoup4"]:  # Lista de pacotes permitidos
                st.write(f"Instalando {package}...")
                result = subprocess.run(['pip', 'install', package], capture_output=True, text=True)
                if result.returncode == 0:
                    st.success(f"{package} instalado com sucesso!")
                    st.write(result.stdout)
                else:
                    st.error(f"Erro ao instalar {package}:")
                    st.write(result.stderr)
            else:
                st.error(f"Pacote '{package}' não permitido ou não reconhecido.")
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