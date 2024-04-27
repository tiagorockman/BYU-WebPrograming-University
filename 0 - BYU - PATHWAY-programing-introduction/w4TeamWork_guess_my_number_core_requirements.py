import random

numero_magico = random.randint(1, 100)
chute = int(input("Qual é o seu chute? "))

while chute != numero_magico:
    if chute < numero_magico:
        print("maior")
    elif chute > numero_magico:
        print("menor")
    chute = int(input("Qual é o seu chute? "))

print("você acertou!")