import streamlit as st
import pandas as pd
import funcoes

st.title("Cadastro de clientes")

nome = st.text_input("Digite seu nome:")
telefone = st.text_input("Digite seu telefone:")
endereco = st.text_input("Digite seu endereço:")

if st.button("Adicionar cliente"):
    funcoes.insertDados(nome, telefone, endereco)
    st.success("Cliente adicionado com sucesso!")

if st.button("Listar clientes"):
    dados = funcoes.listarDados()
    tb = pd.DataFrame(dados, columns=["ID", "Nome", "Telefone", "Endereço"])
    st.table(tb)

st.divider()

id_cliente = st.number_input(
    "Digite o ID do cliente para apagar",
    min_value=0,
    step=1
)

if st.button("Apagar cliente"):
    funcoes.apagarCliente(id_cliente)
    st.success("Cliente apagado com sucesso!")
