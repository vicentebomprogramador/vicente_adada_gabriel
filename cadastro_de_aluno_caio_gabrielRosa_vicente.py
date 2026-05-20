# import mysql.connector
# from mysql.connector import Error

# def criar_conexao():

#     try:
#         conexao = mysql.connector.connect(
#             host='127.0.0.1',
#             user='root',
#             password='Senac2026',
#             database='sistema_escolar'
#         )
#         return conexao
#     except Error as e:
#         print(f"Erro ao conectar ao MySQL: {e}")
#         return None
    
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
            print("/////////////////////////")
            print("não há alunos cadastrados")
            print("/////////////////////////")
            return

        print("Lista de alunos:")
        for i in range(len(alunos)):
            print(f"{i+1} - Nome: {alunos[i]} | Turma: {turma[i]}")

        matricula = input("Digite a matrícula do aluno que deseja remover: ").strip()

        if not matricula.isdigit():
            print("///////////////////")
            print("matrícula inválida")
            print("///////////////////")
            continue  

        indice = int(matricula) - 1

        if indice < 0 or indice >= len(alunos):
            print("////////////////////////")
            print("matrícula não encontrada")
            print("////////////////////////")
            continue  

        print(f"Removendo aluno {alunos[indice]}...")

        alunos.pop(indice)
        turma.pop(indice)

        print("Aluno removido com sucesso!")
        break 

def registrar_notas():




    while True:
        try:
            trabalho = float(input("nota trabalho (0-10): "))
            if trabalho < 0 or trabalho > 10:
                print("nota inválida")
                continue
            break
        except:
            print("digite número válido")

    while True:
        try:
            prova = float(input("nota prova (0-10): "))
            if prova < 0 or prova > 10:
                print("nota inválida")
                continue
            break
        except:
            print("digite número válido")


    print("notas registradas com sucesso!")
    
    return trabalho, prova

def situacao_aluno(trabalho, prova):
    media = (trabalho + prova) / 2

    print(f"Média: {media:.1f}")

    if media >= 7:
        print("Aluno aprovado")
    elif media >= 5:
        print("Aluno em recuperação")
    else:
        print("Aluno reprovado")
        











cadastrar_aluno()
registrar_notas()
apagar_aluno()
trabalho, prova = registrar_notas()
situacao_aluno(trabalho, prova)