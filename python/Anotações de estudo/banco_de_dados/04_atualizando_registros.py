import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()


def criar_tabela(conexao, cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTERGER PRIMARY KEY AUTOINCREMENTE, none VARCHAR(100), email VARCHAR)"
    )
    conexao.commit()


def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES(?,?);", data)
    conexao.commit()
    

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()


criar_tabela(conexao, cursor)

# Testar a inserção para garantir que há um registro com id=1
inserir_registro(conexao, cursor, "joao", "joao@gmail.com")

atualizar_registro(conexao, cursor, "joao", "gustavo@gmail.com", 1)
