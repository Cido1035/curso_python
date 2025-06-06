


# Pedir a largura e o comprimento do terreno.

# Calcular a área em metros quadrados.

# Perguntar o preço do metro quadrado.

# Calcular e mostrar o valor total do terreno.


# print("=== Calculadora de Área e Preço do Terreno ===")

# Entradas
# largura = float(input("Digite a largura do terreno (em metros): "))
# comprimento = float(input("Digite o comprimento do terreno (em metros): "))
    
# # Cálculo da área
# area = largura * comprimento
# print(f"A área total é: {area:.2f} m²")

# # Preço por metro quadrado
# preco_m2 = float(input("Digite o preço por metro quadrado (R$): "))

# # Cálculo do valor total
# valor_total = area * preco_m2
# print(f"O valor total do terreno é: R${valor_total:.2f}")


produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade: "))
preco_unitario = float(input("Digite o preço unitário (R$): "))

total = quantidade * preco_unitario

print(f"=cupom fiscal=:") 
input(f"nome do cliente")

print(f"\nProduto: {produto}")
print(f"Quantidade: {quantidade}")
print(f"Preço unitário: R${preco_unitario:.2f}")
print(f"Total: R${total:.2f}")