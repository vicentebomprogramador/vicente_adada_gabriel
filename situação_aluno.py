from cadastro_de_aluno_caio_gabrielRosa_vicente import *

def situacao_aluno(trabalho, prova):
    media = (trabalho + prova) / 2

    print(f"Média: {media:.1f}")

    if media >= 7:
        print("Aluno aprovado")
    elif media >= 5:
        print("Aluno em recuperação")
    else:
        print("Aluno reprovado")
        


situacao_aluno(trabalho, prova)