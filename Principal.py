from Menu import *
from Listar import *
from Atualizar import*

def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Senac2026',
            database='sistema_escolar'
        )
        return conexao

    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None
    
atualizar_aluno()
listar_alunos()
menu()