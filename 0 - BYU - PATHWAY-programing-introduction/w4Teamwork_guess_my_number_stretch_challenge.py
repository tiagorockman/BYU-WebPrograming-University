import random

print()
print("#################################")
print("Bem-vindo ao Jogo da Adivinhação!")
print("#################################")

continuar_jogando = True
while continuar_jogando:
    numero_magico = random.randint(1, 100)
    chute = int(input("Qual é o seu chute? "))
    qtd_de_chutes = 1

    while chute != numero_magico:
        if chute < numero_magico:
            print("maior")
        elif chute > numero_magico:
            print("menor")
        chute = int(input("Qual é o seu chute? "))
        qtd_de_chutes += 1

    print("#################################")
    print(f"Você acertou após {qtd_de_chutes} chutes!")
    resposta = input("Você deseja continuar jogando? (sim/não) ")
    continuar_jogando = resposta.lower() == "sim"
    print()

print("#################################")