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
    nomes = input("qual é o nome do aluno que voce deseja cadastrar?: ")
    if nomes == "":
        print("não pode campo vazio")
        return

    elif not nomes.isalpha():
        print("nome inválido...")
        return 
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
        print(f"sua matricula é: {matricula}")
        turma.append(turmas)
        alunos.append(nomes)
        
        



def apagar_aluno():
    while True:
        if not alunos:
            print("não há alunos cadastrados")
            continue
        print("deseja apagar um usuario?")
        print("sim/yes/s \nnão/no/n")
        escolha = input().lower

        if not escolha().strip():
            print("campo vazio, tente novamente") 
            continue
        if escolha() in ("sim" "yes" "s"):
            print("qual a matricula do aluno que você deseja apagar?")
            matricula_aluno = input()
            if matricula_aluno.isdigit() == False:
                print("ERRO: matricula te q ser um numero")
                continue

            else:
                alunos.pop(matricula_aluno - 1)
                print("Aluno apagado com sucesso!")
            

        
            
        elif escolha() in ("não" "no" "n"):
            break
        else:
            print("///////////////\nescolha uma das opções\n///////////////")
            continue






cadastrar_aluno()
apagar_aluno()