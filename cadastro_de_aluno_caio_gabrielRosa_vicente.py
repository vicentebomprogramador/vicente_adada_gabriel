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

    print("=== ESCOLHA O ATOR ===")
    print("1 - aluno")
    print("2 - professor")
    print("3 - diretor")

    ator = input("quem é você? ").strip()

    while True:

        print("\n=== MENU ===")

        if ator == "1":

            print("1 - cadastrar aluno")
            print("2 - calcular media")
            print("0 - sair")

            opcao = input("escolha uma opção: ").strip()

            if opcao == "1":
                cadastrar_aluno()

            elif opcao == "2":
                calcular_media()

            elif opcao == "0":
                print("saindo...")
                break

            else:
                print("opção inválida.")

        elif ator == "2":

            print("1 - registrar notas")
            print("2 - atualizar aluno")
            print("3 - calcular media")
            print("4 - situação do aluno")
            print("0 - sair")

            opcao = input("escolha uma opção: ").strip()

            if opcao == "1":
                registrar_notas()

            elif opcao == "2":
                atualizar_aluno()

            elif opcao == "3":
                calcular_media()

            elif opcao == "4":
                situação_aluno()

            elif opcao == "0":
                print("saindo...")
                break

            else:
                print("opção inválida.")

        elif ator == "3":

            print("1 - listar alunos")
            print("2 - apagar aluno")
            print("0 - sair")

            opcao = input("escolha uma opção: ").strip()

            if opcao == "1":
                listar_alunos()

            elif opcao == "2":
                apagar_aluno()

            elif opcao == "0":
                print("saindo...")
                break

            else:
                print("opção inválida.")

        else:
            print("ator inválido.")
            break


menu()