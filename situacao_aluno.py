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



while True:
    nome = input("Nome do aluno: ").strip().lower()
    sobrenome = input("Sobrenome: ").strip().lower()

    if nome == "" or sobrenome == "":
        print("Campo vazio")
        continue

    if not nome.isalpha() or not sobrenome.isalpha():
        print("Nome inválido")
        continue

    break

while True:
    print("\nOpções de turma:")
    print("1 a 9")

    turma = input("Turma: ")

    if turma in ["1","2","3","4","5","6","7","8","9"]:
        break

    print("Turma inválida")

cursor.execute("""
INSERT INTO alunos (nome, sobrenome, turma)
VALUES (%s, %s, %s)
""", (nome, sobrenome, turma))

conexao.commit()

matricula = cursor.lastrowid

print("\nAluno cadastrado com sucesso!")
print(f"Matrícula do aluno: {matricula}")



cursor.execute("""
SELECT matricula
FROM alunos
WHERE matricula = %s
""", (matricula,))

resultado = cursor.fetchone()

if resultado:

    while True:
        print("\nQual matéria?")
        print("L - Levantamento de requisitos")
        print("D - Desenvolver algoritmos")
        print("B - Banco de Dados")

        materia = input("Opção: ").upper()

        if materia == "L":
            materia_id = 1
            break

        elif materia == "D":
            materia_id = 2
            break

        elif materia == "B":
            materia_id = 3
            break

        else:
            print("Matéria inválida")

    while True:
        try:
            nota1 = float(input("Nota trabalho (0-10): "))
            if 0 <= nota1 <= 10:
                break
            print("Nota inválida")
        except:
            print("Digite um número válido")

    while True:
        try:
            nota2 = float(input("Nota prova (0-10): "))
            if 0 <= nota2 <= 10:
                break
            print("Nota inválida")
        except:
            print("Digite um número válido")

    cursor.execute("""
    INSERT INTO notas (matricula, materia_id, nota1, nota2)
    VALUES (%s, %s, %s, %s)
    """, (matricula, materia_id, nota1, nota2))

    conexao.commit()

    print("\nNotas registradas com sucesso!")


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
            print("Situação: APROVADO")
        else:
            print("Situação: REPROVADO")

cursor.close()
conexao.close()