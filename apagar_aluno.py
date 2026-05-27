from cadastro_de_aluno_caio_gabrielRosa_vicente import *


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

apagar_aluno( )