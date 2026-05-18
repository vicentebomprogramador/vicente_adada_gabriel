import mysql.connector
from mysql.connector import Error

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
    
def atualizar_aluno():

    matricula_aluno = int(input("digite a matricula do aluno: "))

    print("1 - atualizar nome")
    print("2 - atualizar turma")

    escolha = input("escolha: ")

    if escolha == "1":

        novo_nome = input("novo nome: ")

        print("nome atualizado!")

    elif escolha == "2":

        nova_turma = input("nova turma: ")

        print("turma atualizada!")

    else:
        print("opção inválida")


def listar_alunos():

    dados = []

    if len(dados) == 0:
        print("nenhum aluno cadastrado")

    else:

        print("\n=== lista de alunos ===")

        for aluno in dados:

            print("matricula:", aluno[0])
            print("nome:", aluno[1])
            print("turma:", aluno[2])
            print()


def menu():

    while True:

        print("\n=== MENU ===")
        print("1 - cadastrar aluno")
        print("2 - registrar notas")
        print("3 - situação do aluno")
        print("4 - atualizar aluno")
        print("5 - apagar aluno")
        print("6 - listar alunos")
        print("0 - sair")

        opcao = input("escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_aluno()

        elif opcao == "2":
            registrar_notas()

        elif opcao == "3":
            situação_aluno()

        elif opcao == "4":
            atualizar_aluno()

        elif opcao == "5":
            apagar_aluno()

        elif opcao == "6":
            listar_alunos()

        elif opcao == "0":
            print("saindo...")
            break

        else:
            print("opção inválida.")


menu()