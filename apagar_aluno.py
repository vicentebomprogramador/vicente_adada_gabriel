from cadastro_de_aluno_caio_gabrielRosa_vicente import *
import mysql.connector

def apagar_aluno():
    try:
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Senac2026",
            database="projeto_final"
        )

        cursor = conexao.cursor()

        cursor.execute("SELECT matricula, nome, turma FROM alunos")
        alunos = cursor.fetchall()

        if not alunos:
            print("/////////////////////////")
            print("Não há alunos cadastrados")
            print("/////////////////////////")
            return

        print("\nLista de alunos:")
        for aluno in alunos:
            print(f"Matrícula: {aluno[0]} | Nome: {aluno[1]} | Turma: {aluno[2]}")

        matricula = input("\nDigite a matrícula do aluno que deseja remover: ")

        cursor.execute(
        "DELETE FROM notas WHERE matricula = %s",
        (matricula,)
        )


        cursor.execute(
        "DELETE FROM alunos WHERE matricula = %s",
        (matricula,)
        )   

        conexao.commit()

        if cursor.rowcount > 0:
            print("/////////////////////////")
            print("Aluno removido com sucesso!")
            print("/////////////////////////")
        else:
            print("/////////////////////////")
            print("Matrícula não encontrada")
            print("/////////////////////////")
        return
    except mysql.connector.Error as erro:
        print(f"Erro: {erro}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

apagar_aluno()