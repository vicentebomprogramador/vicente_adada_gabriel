from cadastro_de_aluno_caio_gabrielRosa_vicente import *

import mysql.connector

conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Senac2026",
    database="projeto_final"
)

cursor = conexao.cursor()

matricula = input("Digite a matrícula do aluno: ")

cursor.execute("""
SELECT nota1, nota2
FROM notas
WHERE matricula = %s
""", (matricula,))

notas = cursor.fetchall()

if len(notas) == 0:
    print("Aluno não encontrado.")
else:
    for nota1, nota2 in notas:
        media = (nota1 + nota2) / 2

        print(f"\nNota trabalho: {nota1}")
        print(f"Nota prova: {nota2}")
        print(f"Média: {media:.1f}")

        if media >= 7:
            print("Situação: APROVADO")
        else:
            print("Situação: REPROVADO")

cursor.close()
conexao.close()