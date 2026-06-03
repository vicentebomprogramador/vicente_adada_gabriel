import mysql.connector
from mysql.connector import Error
from materias import calcular_media_situacao


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

    if not resultado:
       print("aluno não encontrado")
       return
    
    matricula = resultado[0]


    while True:
        print("qual matéria?")
        print("opções:")
        print("L - Levantamento de requisitos")
        print("D - Desenvolver algoritmos")
        print("B - Banco de Dados")
        materia_escolhida = input()
        if materia_escolhida == ("L"):
          materia_escolhida = "Levantamento de requisitos"
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

        elif materia_escolhida == ("B"):
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
                    if nota2 < 0 or nota2 > 10:
                        print("nota inválida")
                        continue
                    break
                except:
                    print("digite número válido")
        else:
          print("matéria inválida")
          continue
        
        print(matricula)

        cursor.execute("""
        INSERT INTO notas (matricula, nota1, nota2)
        VALUES (%s, %s, %s)
        """, (matricula, nota1, nota2))

        conexao.commit()

        media, situacao = calcular_media_situacao(nota1, nota2)

        print("\nNotas registradas com sucesso!")
        print(f"Nota 1: {nota1}")
        print(f"Nota 2: {nota2}")
        print(f"Média: {media:.1f}")
        print(f"Situação: {situacao}")

        break


    
cadastrar_aluno()
registrar_notas()