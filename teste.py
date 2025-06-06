
# # 1)Crie um jogo perdra, papel e tesoura
# # Onde:
# # Pedra ganha de tesoura;
# # Papel ganha de pedra;
# # Tesoura ganha de Pedra;
# # 2)Crie um jogo com dois jogadores. Onde cada um escolhe entre ímpar ou par.
# # 3)Crie um jogo de adivinhar um número.
# # Gere um número entre 1 e 5 e peça ao jogador, Caso ele acerte. Mostre a mensagem “Você
# # ganhou” senão “Não foi desta vez”import randomcls


# import random

# print("Jogo: Pedra, Papel ou Tesoura")
# print("Escolha: [1] Pedra  [2] Papel  [3] Tesoura")
# 2
# # Entrada do jogador
# jogador = int(input("Digite sua escolha (1, 2 ou 3): "))

# # Jogada do computador (aleatória)
# computador = random.randint(1, 3)

# # Traduzir número para texto
# opcoes = {1: "Pedra", 2: "Papel", 3: "Tesoura"}
# print(f"\nVocê escolheu: {opcoes[jogador]}")
# print(f"Computador escolheu: {opcoes[computador]}")

# # Lógica do jogo

# if jogador == computador:
#     print("Empate!")
# elif (jogador == 1 and computador == 3) or \
#      (jogador == 2 and computador == 1) or \
#      (jogador == 3 and computador == 2):
#     print("Você venceu! 🎉")
# else:
#     print("Você perdeu! 😢")




# jogo de par ou impar

# Crie um jogo com dois jogadores. Onde cada um escolhe entre ímpar ou par.

print("=== Jogo: Ímpar ou Par ===")

# Jogador 1 escolhe ímpar ou par
jogador1_nome = input("Jogador 1, digite seu nome: ")
jogador2_nome = input("Jogador 2, digite seu nome: ")

escolha1 = input(f"{jogador1_nome}, escolha 'ímpar' ou 'par': ").strip().lower()
if escolha1 == "par":
    escolha2 = "ímpar"
else:
    escolha2 = "par"

# Jogadores escolhem números
numero1 = int(input(f"{jogador1_nome}, digite seu número: "))
numero2 = int(input(f"{jogador2_nome}, digite seu número: "))

# Soma e verificação
soma = numero1 + numero2
resultado = "par" if soma % 2 == 0 else "ímpar"

print("\n--- Resultado ---")
print(f"{jogador1_nome} escolheu: {escolha1}")
print(f"{jogador2_nome} ficou com: {escolha2}")

print(f"Números jogados: {numero1} + {numero2} = {soma} ({resultado})")

# Verifica vencedor
if resultado == escolha1:
    print(f"{jogador1_nome} venceu! 🎉")
else:
    print(f"{jogador2_nome} venceu! 🎉")