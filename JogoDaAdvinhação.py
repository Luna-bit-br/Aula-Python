import random

numero_secreto = random.randint(1, 10)

chute = int(input("Advinhe qual o número de 0 à 10!"))

if chute == numero_secreto:
    print("Parabéns você acertou!")
    exit
elif chute > numero_secreto:
    print("Você errou! O Número secreto era menor")
elif chute < numero_secreto:
    print("Você errou! O Número secreto era maior")

segundo_chute = int(input("Segunda tentativa para advinhar qual o número de 0 à 10!"))

if segundo_chute == numero_secreto:
    print("Você Acertou!")
else:
    print(f"Você errou! O número era {numero_secreto}")