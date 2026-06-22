from cadastrar import *

import mysql.connector

conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Senac2026",
    database="projeto_final"
)

cursor = conexao.cursor()
def situacao_aluno():

    matricula = input("Digite a matrícula do aluno: ")

    cursor.execute("""
    SELECT materias.nome, notas.nota1, notas.nota2
    FROM notas
    JOIN materias ON notas.materia_id = materias.id
    WHERE notas.matricula = %s
    """, (matricula,))

    dados = cursor.fetchall()

    if len(dados) == 0:
        print("Aluno não encontrado.")
        return

    for materia, nota1, nota2 in dados:
        media = (nota1 + nota2) / 2

        print(f"\nMatéria: {materia}")
        print(f"Nota trabalho: {nota1}")
        print(f"Nota prova: {nota2}")
        print(f"Média: {media:.1f}")

        if media >= 7:
            print("Situação: APROVADO")
        else:
            print("Situação: REPROVADO")
