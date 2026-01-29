# =====================================================
# APOSTILA PRÁTICA – PYTHON PARA INICIANTES
# =====================================================


# -----------------------------------------------------
# 1) ENTRADA E SAÍDA DE DADOS
# -----------------------------------------------------
"""
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

print("Olá,", nome)
print(f"Você tem, {idade} anos")
"""

# -----------------------------------------------------
# 2) CALCULADORA SIMPLES (SOMA)
# -----------------------------------------------------
"""
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
print("A soma é:", soma)
"""


# -----------------------------------------------------
# 3) VERIFICAÇÃO DE MAIORIDADE
# -----------------------------------------------------
"""
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade")
    print("MEUS PARABÉNS")
else:
    print("Você é menor de idade")
"""


# -----------------------------------------------------
# 4) NÚMERO PAR OU ÍMPAR
# -----------------------------------------------------
"""
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("Número par")
else:
    print("Número ímpar")
"""


# -----------------------------------------------------
# 5) CONTADOR COM WHILE
# -----------------------------------------------------
"""
contador = 1

while contador <= 10:
    print(contador)
    contador += 1
"""


# -----------------------------------------------------
# 6) TABUADA COM FOR
# -----------------------------------------------------
"""
numero = float(input("Digite um número: "))

for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)

"""

# -----------------------------------------------------
# 7) LISTA DE NOMES
# -----------------------------------------------------
"""
nomes = []

for i in range(3):
    nome = input("Digite um nome: ")
    nomes.append(nome)

print("Nomes cadastrados:")
print(nomes)
"""


# -----------------------------------------------------
# 8) CADASTRO DE ALUNO (LISTA + DICIONÁRIO)
# -----------------------------------------------------

alunos = []

nome = input("Nome do aluno: ")
idade = int(input("Idade: "))
nota = float(input("Nota: "))

aluno = {
    "nome": nome,
    "idade": idade,
    "nota": nota
}

alunos.append(aluno)

print("\n Alunos cadastrados: \n")
print(alunos)



# -----------------------------------------------------
# 9) FUNÇÃO SIMPLES
# -----------------------------------------------------
"""
def saudacao(nome):
    print("Olá,", nome)

saudacao("Maria")
saudacao("João")
"""


# -----------------------------------------------------
# 10) FUNÇÃO COM RETORNO (SOMA)
# -----------------------------------------------------
"""
def soma(a, b):
    return a + b

resultado = soma(5, 3)
print("Resultado:", resultado)
"""


# -----------------------------------------------------
# 11) JOGO DE ADIVINHAÇÃO
# -----------------------------------------------------
"""
import random

numero_secreto = random.randint(1, 10)

while True:
    chute = int(input("Digite um número entre 1 e 10: "))

    if chute == numero_secreto:
        print("Você acertou!")
        break
    else:
        print("Tente novamente")
"""


# -----------------------------------------------------
# 12) MENU SIMPLES
# -----------------------------------------------------
"""
while True:
    print("1 - Dizer Olá")
    print("2 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Olá, usuário!")
    elif opcao == "2":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida")
"""
