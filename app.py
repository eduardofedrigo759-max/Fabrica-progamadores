import streamlit as st
from pathlib import Path

st.title("Fedrigo Automóveis - Aluguel de Carros")

lista_carros = [
    "Fox",
    "Toro",
    "Uno",
    "Puro Sangue",
    "Bugatti",
    "Mustang"
]

# Localiza o logo na mesma pasta do app.py
logo = Path(__file__).parent / "logo.png"

st.image(str(logo), width=300)

opcao = st.sidebar.selectbox(
    "Escolha seu carro:",
    lista_carros
)

st.write("Você escolheu:", opcao)