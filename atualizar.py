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


def atualizar_aluno():

    matricula_aluno = int(input("digite a matricula do aluno: "))

    print("1 - atualizar nome")
    print("2 - atualizar turma")

    escolha = input("escolha: ")

    conexao = criar_conexao()

    if conexao:

        cursor = conexao.cursor()

        if escolha == "1":

            novo_nome = input("novo nome: ")
            novo_sobrenome = input("novo sobrenome: ")

            sql = "UPDATE alunos SET nome = %s, sobrenome = %s WHERE matricula = %s"

            valores = (novo_nome, novo_sobrenome, matricula_aluno)

            cursor.execute(sql, valores)

            conexao.commit()

            print("nome e sobrenome atualizados!")

        elif escolha == "2":

            nova_turma = input("nova turma: ")

            sql = "UPDATE alunos SET turma = %s WHERE matricula = %s"

            valores = (nova_turma, matricula_aluno)

            cursor.execute(sql, valores)

            conexao.commit()

            print("turma atualizada!")

        else:
            print("opção inválida")

        