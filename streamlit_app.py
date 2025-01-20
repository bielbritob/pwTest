import streamlit as st
import subprocess

# Inicializa a variável de sessão
if "first_run" not in st.session_state:
    st.session_state.first_run = True

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
