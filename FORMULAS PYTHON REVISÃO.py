#Função Print Mostra escrito o valor entre as aspas no terminal
print("Olá, mundo!")

#Variáveis
nome = "Pedro"
idade = 20

#Input de Dados
nome = input("Digite seu nome: ")
print("Olá,", nome, ", Tudo bem?")

#Condicionais (if/else)
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

#Função Sem valor
def saudacao():
    print("Olá! Seja bem-vindo!")
saudacao()

#Função COM parametro
def mostrar_nome(nome):
    print("Seu nome é:", nome)
mostrar_nome("Carlos")

#Função que retorna valores
def soma(a, b):
    return a + b
resultado = soma(5, 7)
print("A soma é:", resultado)
"""
#Loop FOR
for i in range(1, 6):
    print(i)

#Loop WHILE
contador = 1
while contador <= 5:
    print(contador)
contador += 1
"""
