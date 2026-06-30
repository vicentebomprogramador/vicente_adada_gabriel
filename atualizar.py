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

    while True:
        try:
            matricula_aluno = int(input("Digite a matrícula do aluno: "))
            break
        except ValueError:
            print("Digite apenas números na matrícula.")

    conexao = criar_conexao()

    if conexao:
        cursor = conexao.cursor()

        sql_verificar = "SELECT * FROM alunos WHERE matricula = %s"
        cursor.execute(sql_verificar, (matricula_aluno,))

        resultado = cursor.fetchone()

        if resultado is None:
            print("/////////////////////////")
            print("Matrícula não encontrada")
            print("/////////////////////////")
            return

        print("1 - atualizar nome")
        print("2 - atualizar turma")

        escolha = input("Escolha: ")

        if escolha == "1":

            novo_nome = input("Novo nome: ")
            novo_sobrenome = input("Novo sobrenome: ")

            sql = """
            UPDATE alunos
            SET nome = %s, sobrenome = %s
            WHERE matricula = %s
            """

            valores = (novo_nome, novo_sobrenome, matricula_aluno)

            cursor.execute(sql, valores)
            conexao.commit()

            print("Nome e sobrenome atualizados!")

        elif escolha == "2":

            nova_turma = input("Nova turma: ")

            sql = """
            UPDATE alunos
            SET turma = %s
            WHERE matricula = %s
            """

            valores = (nova_turma, matricula_aluno)

            cursor.execute(sql, valores)
            conexao.commit()

            print("Turma atualizada!")

        else:
            print("Opção inválida")

        cursor.close()
        conexao.close()

    else:
        print("Erro ao conectar ao banco.")