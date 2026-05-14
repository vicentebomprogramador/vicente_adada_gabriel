import mysql.connector
from mysql.connector import Error

def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Senac2026',
            database='sistema_escolar'
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None
turma = []
matricula = 0
alunos = []
def cadastrar_aluno():
    global matricula
    while True:
        nomes = input("nome do aluno: ")
        sobrenome = input("sobrenome: ")
        if nomes == "":
            print("não pode campo vazio")
            continue
        elif sobrenome == "":
            print("não pode campo vazio")
            continue

        elif not nomes.isalpha():
            print("nome inválido...")
            continue
        elif not sobrenome.isalpha():
            print("sobrenome inválido...")
            continue
        
        else:
            break
    alunos = [nomes, sobrenome]
    aluno = [alunos, turma]
    
               
    while turma == [] or alunos == []:
        print("opções:")
        print("1 - 1 ANO")
        print("2 - 2 ANO")
        print("3 - 3 ANO")
        print("4 - 4 ANO")
        print("5 - 5 ANO")
        print("6 - 6 ANO")
        print("7 - 7 ANO")
        print("8 - 8 ANO")
        print("9 - 9 ANO")
        turmas = input("qual é a turma do aluno?: ")
        
        if turmas == "":
            print("não pode campo vazio")
            continue
        elif turmas == "1":
            print("seja bem-vindo ao primeiro ano na escola, boa sorte ")
        elif turmas == "2":
            print("segundo ano na escola, boa sorte ")
        elif turmas == "3":
            print("terceiro ano na escola, boa sorte ")
        elif turmas == "4":
            print("ta ficando grande hein, boa sorte ")
        elif turmas == "5":
            print("quinto ano o ano da zoeira, boa sorte ")
        elif turmas == "6":
            print("primeiro ano no fundamental 2, boa sorte ")
        elif turmas == "7":
            print("voce é um adolescente, boa sorte ")
        elif turmas == "8":
            print("seja bem-vindo ao oitavo ano na escola, boa sorte ")
        elif turmas == "9":
            print("ultimo ano antes do ensino médio, boa sorte ")
        else:
            print("turma inválida...")
            continue
        matricula += 1
        print(f"a matrícula do aluno é: {matricula}")
        turma.append(turmas)
        alunos.append(nomes, sobrenome)


nota = []
def registrar_notas(alunos, nota):
    
    if len(alunos) == 0:
        print("nenhum aluno cadastrado")
        return
    print ("qual aluno você quer registrar uma nota?")
    
    nome = input("Digite o nome do aluno: ").strip()

    encontrados = []
  










cadastrar_aluno()
cadastrar_aluno()
print(alunos)
registrar_notas(alunos, nota)