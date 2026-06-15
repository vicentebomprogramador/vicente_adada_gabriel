import mysql.connector
from mysql.connector import Error
from registrar_nota import *
from cadastrar import *
import mysql.connector
from mysql.connector import Error

try:
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Senac2026",
        database="projeto_final"
    )

    cursor = conexao.cursor(buffered=True)

except Error as e:
    print(f"Erro ao conectar ao MySQL: {e}")
    exit()


def situacao_aluno():
    matricula = input("Digite a matrícula: ")

    cursor.execute("""
        SELECT nota1, nota2
        FROM notas
        WHERE matricula = %s
    """, (matricula,))

    notas = cursor.fetchall()

    if len(notas) == 0:
        print("Nenhuma nota encontrada.")

    else:
        for nota1, nota2 in notas:

            media = (nota1 + nota2) / 2

            print(f"\nNota 1: {nota1}")
            print(f"Nota 2: {nota2}")
            print(f"Média: {media:.1f}")

            if media >= 7:
                print("APROVADO")
            else:
                print("REPROVADO")