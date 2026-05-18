
        



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