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
else:
    print("Erro de conexão")
    exit()



def cadastrar_aluno():
    while True:
        nome = input("nome do aluno: ").strip().lower()
        sobrenome = input("sobrenome: ").strip().lower()

        if nome == "" or sobrenome == "":
            print("campo vazio")
            continue

        if not nome.isalpha() or not sobrenome.isalpha():
            print("nome inválido")
            continue

        break

    while True:
        print("opções de turma:")
        print("1 a 9")

        turma = input("turma: ")

        if turma in ["1","2","3","4","5","6","7","8","9"]:
            print("turma cadastrada!")
            break
        else:
            print("turma inválida")

    sql = """
    INSERT INTO alunos (nome, sobrenome, turma)
    VALUES (%s, %s, %s)
    """

    valores = (nome, sobrenome, turma)
    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Aluno cadastrado com sucesso!")
    print(f"Matrícula do aluno: {cursor.lastrowid}")



