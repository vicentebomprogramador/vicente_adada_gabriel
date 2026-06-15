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

def apagar_aluno():
    while True:
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
                print("não há alunos cadastrados")
                print("Não há alunos cadastrados")
                print("/////////////////////////")
                return

            print("Lista de alunos:")
            for i in range(len(alunos)):
                print(f"{i+1} - Nome: {alunos[1]} | Turma: {aluno[3]}")
            print("\nLista de alunos:")
            for aluno in alunos:
                print(f"Matrícula: {aluno[0]} | Nome: {aluno[1]} | Turma: {aluno[2]}")

            matricula = input("Digite a matrícula do aluno que deseja remover: ").strip()
            matricula = input("\nDigite a matrícula do aluno que deseja remover: ")

            if not matricula.isdigit():
                print("///////////////////")
                print("matrícula inválida")
                print("///////////////////")
                continue  
            cursor.execute(
            "DELETE FROM notas WHERE matricula = %s",
            (matricula,)
            )

            indice = int(matricula) - 1

            if indice < 0 or indice >= len(alunos):
                print("////////////////////////")
                print("matrícula não encontrada")
                print("////////////////////////")
                continue  
            cursor.execute(
            "DELETE FROM alunos WHERE matricula = %s",
            (matricula,)
            )   

            print(f"Removendo aluno {alunos[indice]}...")
            conexao.commit()

            alunos.pop(indice)
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

            print("Aluno removido com sucesso!")
            break 
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conexao' in locals():
                conexao.close()

   