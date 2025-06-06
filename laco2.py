# Faça um laço que exiba os números da faixa solicitada pelo usuário e diga se é par ou impar. E tudo isto usando laço while.
inicio = 0
fim = 0




while True:
    inicio = int(input("digite o numero inicial: "))
    fim = int(input("digite o numerom final: "))
    if fim > inicio:
        break
    else:
        print("numero inicial tem que ser maior que o final")

while inicio <= fim:
    para_ou_impar = "impar"
    if inicio % 2 == 0:
        para_ou_impar = "par"
          
    print(f"o numero {inicio} é {para_ou_impar}")
    inicio +=1

    
