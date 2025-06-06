produto1 = float (input("valor do produto"))
produto2 = float (input("valor do produto"))
produto3 = float (input("Valor do produto"))

produtos = [ produto1, produto2, produto3]
soma = sum (produtos)

if  soma > 100 :
    desconto =  0.10 * soma
    total =  soma - desconto
    print (f"Desconto de 10% {desconto:.2f}")
    print (f"Valor a pagar {total:.2f}")

if soma < 100 :
    print ("sem desconto")
    print (f"Valor a pagar {soma:.2f}") 


