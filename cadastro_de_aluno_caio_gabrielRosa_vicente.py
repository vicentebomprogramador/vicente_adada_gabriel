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

    print("aluno cadastrado com sucesso!")


def registrar_notas():
    nome = input("nome do aluno: ").strip().lower()
    sobrenome = input("sobrenome: ").strip().lower()

    cursor.execute("""
    SELECT matricula FROM alunos
    WHERE nome=%s AND sobrenome=%s
    """, (nome, sobrenome))

    resultado = cursor.fetchone()

    if resultado is None:
        print("aluno não encontrado")
        return

    matricula = resultado[0]
    while True:
        print("qual matéria?")
        print("\nOpções:")
        print("L - Levantamento de requisitos")
        print("D - Desenvolver algoritmos")
        print("B - Banco de Dados")
        materia_escolhida = input()
        if materia_escolhida == ("L"):
          materia_escolhida = "Levantamento de requisitos"
          materia_id = 1
          while True:
           
           try:
            nota1= float(input("nota trabalho (0-10): "))
            if nota1 < 0 or nota1 > 10:
                print("nota inválida")
                continue
            break
           except:
            print("digite número válido")
            continue
         
                

          while True:
                try:
                    nota2 = float(input("nota prova (0-10): "))
                    if nota2 < 0 or nota2 > 10:
                        print("nota inválida")
                        continue
                    break
                except:
                    print("digite número válido")
        elif materia_escolhida == ("D"):
          materia_escolhida = "Desenvolver algoritmos"
          materia_id = 2
          while True:
           try:
            nota1_ = float(input("nota trabalho (0-10): "))
            if nota1 < 0 or nota1 > 10:
                print("nota inválida")
                continue
            break
           except:
            print("digite número válido")
            continue
            
                

          while True:
                try:
                    nota2 = float(input("nota prova (0-10): "))
                    if nota2 < 0 or nota2 > 10:
                        print("nota inválida")
                        continue
                    break
                except:
                    print("digite número válido")

        elif materia_escolhida == ("B"):
          materia_id = 3
          materia_escolhida = "Banco de dados"
          while True:
           try:
            nota1= float(input("nota trabalho (0-10): "))
            if nota1 < 0 or nota1 > 10:
                print("nota inválida")
                continue
            break
           except:
            print("digite número válido")
            continue
        
        

          while True:
                try:
                    nota2 = float(input("nota prova (0-10): "))
                    if nota2< 0 or nota2 > 10:
                        print("nota inválida")
                        continue
                    break
                except:
                    print("digite número válido")
        
        else:
          print("matéria inválida")
          continue
        
        cursor.execute("""
            INSERT INTO notas (matricula,materia_id, nota1, nota2)
            VALUES (%s, %s, %s, %s)
        """, (matricula,materia_id, nota1, nota2))

 









        conexao.commit()

        print("notas registradas com sucesso!")
        break
cadastrar_aluno()
registrar_notas()