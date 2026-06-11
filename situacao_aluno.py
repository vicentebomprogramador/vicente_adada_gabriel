from cadastro_de_aluno_caio_gabrielRosa_vicente import *

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


def calcular_media_situacao():
    conexao = criar_conexao()

    if not conexao:
        return

    cursor = conexao.cursor()

    matricula = input("Digite a matrícula do aluno: ")

    cursor.execute("""
        SELECT a.nome,
               a.sobrenome,
               m.nome,
               n.nota1,
               n.nota2
        FROM notas n
        JOIN alunos a ON n.matricula = a.matricula
        JOIN materias m ON n.materia_id = m.id
        WHERE a.matricula = %s
    """, (matricula,))

    resultados = cursor.fetchall()

    if not resultados:
        print("Aluno não encontrado ou sem notas cadastradas.")
        return

    print("\n===== BOLETIM =====")

    for nome, sobrenome, materia, nota1, nota2 in resultados:
        media = (nota1 + nota2) / 2

        if media >= 7:
            situacao = "APROVADO"
        else:
            situacao = "REPROVADO"

        print(f"\nAluno: {nome.title()} {sobrenome.title()}")
        print(f"Matéria: {materia}")
        print(f"Nota 1: {nota1}")
        print(f"Nota 2: {nota2}")
        print(f"Média: {media:.1f}")
        print(f"Situação: {situacao}")

    cursor.close()
    conexao.close()


calcular_media_situacao()