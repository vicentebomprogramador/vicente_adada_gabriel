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


def listar_alunos():

    conexao = criar_conexao()

    if conexao:

        cursor = conexao.cursor()

        sql = "SELECT * FROM alunos"

        cursor.execute(sql)

        dados = cursor.fetchall()

        if len(dados) == 0:
            print("nenhum aluno cadastrado")

        else:

            print("\n=== lista de alunos ===")

            for aluno in dados:

                print("matricula:", aluno[0])
                print("nome:", aluno[1])
                print("turma:", aluno[2])
                print()

        cursor.close()
        conexao.close()


