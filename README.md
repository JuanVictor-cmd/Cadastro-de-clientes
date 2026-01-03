# 🧾 Cadastro de Clientes com Streamlit e SQLite

## 📌 Visão Geral

Este projeto é uma aplicação simples de **CRUD (Create, Read, Delete)** desenvolvida em **Python**, utilizando **SQLite** como banco de dados e **Streamlit** como interface web.

A aplicação permite realizar o **cadastro, listagem e exclusão de clientes**, armazenando os dados localmente em um banco SQLite. O foco do projeto é demonstrar conceitos fundamentais de persistência de dados, modularização de código e criação de interfaces interativas.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **SQLite3** – Banco de dados local
* **Streamlit** – Interface web interativa
* **Pandas** – Exibição de dados em tabela

---

## 📂 Estrutura de Arquivos

```
📁 projeto
 ├── Clientes.db
 ├── funcoes.py
 ├── interface.py
 └── README.md
```

* **Clientes.db**: Banco de dados SQLite
* **funcoes.py**: Funções de conexão e operações no banco de dados
* **interface.py**: Interface gráfica desenvolvida com Streamlit

---

## ⚙️ Funcionalidades

### 🔹 1. Criação do Banco de Dados

* Criação automática do banco `Clientes.db`
* Criação da tabela **Cliente** com os campos:

  * ID (chave primária autoincrementável)
  * Nome
  * Telefone
  * Endereço

---

### 🔹 2. Conexão com o Banco

A aplicação utiliza uma função centralizada para conexão com o banco de dados:

* Facilita manutenção
* Evita repetição de código
* Garante abertura e fechamento correto das conexões

---

### 🔹 3. Cadastro de Clientes (Create)

* Inserção de novos clientes no banco de dados
* Dados coletados via formulário interativo no Streamlit
* Confirmação visual após o cadastro

---

### 🔹 4. Listagem de Clientes (Read)

* Consulta de todos os clientes cadastrados
* Exibição em formato de tabela utilizando Pandas
* Atualização dinâmica na interface

---

### 🔹 5. Exclusão de Clientes (Delete)

* Exclusão de clientes a partir do **ID**
* Validação por campo numérico
* Confirmação visual após exclusão

---

## 💡 Diferenciais do Projeto

* Implementação clara do padrão **CRUD**
* Separação entre lógica de negócio e interface
* Uso de banco de dados local sem dependências externas
* Interface simples e intuitiva
* Ideal para estudos iniciais em backend e persistência de dados

---

## 🚀 Possíveis Melhorias Futuras

* Implementação de atualização de clientes (Update)
* Validações de formulário
* Confirmação antes de apagar registros
* Pesquisa e filtros por nome ou telefone
* Migração para bancos como PostgreSQL ou MySQL
* Autenticação de usuários

---

## ▶️ Como Executar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Instale as dependências:

```bash
pip install streamlit pandas
```

3. Execute a aplicação:

```bash
streamlit run interface.py
```

---

## 🧾 Conclusão

Este projeto demonstra de forma prática como integrar **SQLite**, **Python** e **Streamlit** para criar aplicações simples com persistência de dados. Ele evidencia conceitos fundamentais de banco de dados, organização de código e construção de interfaces, sendo ideal para portfólio iniciante ou projetos educacionais.

---

👨‍💻 Desenvolvido por **Juan Victor Almeida de Souza**
