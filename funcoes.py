import sqlite3

def conectaBD():
    conexao = sqlite3.connect("Clientes.db")
    return conexao

def insertDados(nome, telefone, endereco):
    conexao = conectaBD()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Cliente(nome, telefone, endereco) VALUES (?, ?, ?)",(nome, telefone, endereco))
    conexao.commit()
    conexao.close()

def listarDados():
    conexao = conectaBD()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Cliente")    
    dados = cursor.fetchall()
    cursor.close()
    return dados

def apagarCliente(id_cliente):
    conexao = conectaBD()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Cliente WHERE ID = ?", (id_cliente,))
    conexao.commit()
    conexao.close()