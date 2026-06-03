
def calcular_media_situacao(nota1, nota2):
    media = (nota1 + nota2) / 2

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    return media, situacao                

