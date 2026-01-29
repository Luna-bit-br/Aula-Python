for i in range(0):
    print("Olá Mundo!")
    nome = input("Qual seu nome?") #Variavel do nome
    idade = int(input("Qual sua idade?"))
    a = int(input("Digite um número para A?"))
    b = int(input("Digite um número para B?"))

    maioridade = ""
    if idade >= 21: 
        maioridade = "Maior ou igual de 21 anos"
    elif idade >= 18:
        maioridade = "Maior ou igual de 18 anos"
    else:
        maioridade = "Menor de 18 anos"

    def mais(a,b):
        return a + b ** a
    print(f"Olá {nome}, você tem {idade} anos! Pelo visto você tem idade {maioridade}!")    
    print(f"O resultado da conta A + B = {mais(a,b)}")

frutas = ["Maçã", "Banana", "Uva"]
    
frutas.append("pera")       # Adiciona um item ao final
frutas.remove("Banana")     # Remove um item específico
frutas.insert(1, "laranja") # Adiciona em uma posição específica
print(len(frutas))          # Quantos itens tem na lista
for frutas in frutas:
    print("Eu gosto de", frutas)