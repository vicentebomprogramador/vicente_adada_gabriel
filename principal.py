from cadastrar import cadastrar_aluno
from apagar_aluno import apagar_aluno
from situacao_aluno import situacao_aluno
from menu import menu
from listar import listar_alunos
from registrar_nota import registrar_notas
from atualizar import atualizar_aluno

import mysql.connector
from mysql.connector import Error


def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Senac2026',
            database='projeto_final'
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None


conexao = criar_conexao()

if conexao:
    cursor = conexao.cursor(buffered=True)
    cursor = conexao.cursor(buffered=True) 
else:
    print("Erro de conexão")
    exit()



menu()