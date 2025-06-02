
nota1 = float (input ("Digitar uma nota"))
nota2 = float (input ("Digitar uma nota"))
nota3 = float (input ("Digitar uma nota"))
notas = [nota1, nota2, nota3]

soma = sum(notas)
media = soma / len(notas)

if media >= 7:
    print ("APROVADO")
elif media <= 4:
    print ("REPROVADO")
else:
    print ("RECUPERAÇÃO")
