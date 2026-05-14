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


def cadastrar_aluno():

    nomes = input("qual é o nome do aluno que voce deseja cadastrar?: ")

    if nomes == "":
        print("não pode campo vazio")
        return

    elif not nomes.isalpha():
        print("nome inválido...")
        return

    while True:

        print("opções:")
        print("1 - 1 ANO")
        print("2 - 2 ANO")
        print("3 - 3 ANO")
        print("4 - 4 ANO")
        print("5 - 5 ANO")
        print("6 - 6 ANO")
        print("7 - 7 ANO")
        print("8 - 8 ANO")
        print("9 - 9 ANO")

        turmas = input("qual é a turma do aluno?: ")

        if turmas == "":
            print("não pode campo vazio")
            continue

        elif turmas == "1":
            print("seja bem-vindo ao primeiro ano na escola, boa sorte ")

        elif turmas == "2":
            print("segundo ano na escola, boa sorte ")

        elif turmas == "3":
            print("terceiro ano na escola, boa sorte ")

        elif turmas == "4":
            print("ta ficando grande hein, boa sorte ")

        elif turmas == "5":
            print("quinto ano o ano da zoeira, boa sorte ")

        elif turmas == "6":
            print("primeiro ano no fundamental 2, boa sorte ")

        elif turmas == "7":
            print("voce é um adolescente, boa sorte ")

        elif turmas == "8":
            print("seja bem-vindo ao oitavo ano na escola, boa sorte ")

        elif turmas == "9":
            print("ultimo ano antes do ensino médio, boa sorte ")

        else:
            print("turma inválida...")
            continue

        conexao = criar_conexao()

        if conexao:

            cursor = conexao.cursor()

            sql = "INSERT INTO alunos (nome, turma) VALUES (%s, %s)"

            valores = (nomes, turmas)

            cursor.execute(sql, valores)

            conexao.commit()

            print("aluno cadastrado no banco!")

            print("matricula:", cursor.lastrowid)

            cursor.close()
            conexao.close()

        break


def registrar_notas():
    print("qual aluno você quer registrar uma nota")


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

            sql = "UPDATE alunos SET nome = %s WHERE matricula = %s"

            valores = (novo_nome, matricula_aluno)

            cursor.execute(sql, valores)

            conexao.commit()

            print("nome atualizado!")

        elif escolha == "2":

            nova_turma = input("nova turma: ")

            sql = "UPDATE alunos SET turma = %s WHERE matricula = %s"

            valores = (nova_turma, matricula_aluno)

            cursor.execute(sql, valores)

            conexao.commit()

            print("turma atualizada!")

        else:
            print("opção inválida")

        cursor.close()
        conexao.close()


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