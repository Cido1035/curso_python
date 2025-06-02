
def receber_input_usuario():
    nota1 = float (input ("Digitar uma nota"))
    nota2 = float (input ("Digitar uma nota"))
    nota3 = float (input ("Digitar uma nota"))
    return nota1, nota2, nota3

def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media

def verificar_aprovacao(media):
    if media >= 7:
        print ("APROVADO")
    elif media <= 4:
        print ("REPROVADO")
    else:
        print ("RECUPERAÇÃO")


def principal():
    notas = receber_input_usuario()
    media = calcular_media(notas)
    verificar_aprovacao(media)


if __name__ == "__main__": # se o arquivo for executado diretamente, chama a função principal
    principal()