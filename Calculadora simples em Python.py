# Calculadora simples em Python

# 1 Entrada de dados
# O usuário digita dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# O usuário escolhe a operação
operacao = input("Escolha a operação (+, -, *, /): ")

# 2 Processamento (decisão com if/elif/else)
if operacao == "+":
    resultado = num1 + num2
    print("Resultado:", resultado)

elif operacao == '-':
    resultado = num1 - num2
    print("Resultado:", resultado)

elif operacao == '*':
    resultado = num1 * num2
    print("Resultado:", resultado)

elif operacao == '/':
    # Tratamento para divisão por zero
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado:", resultado)
    else:
        print("Erro: não é possível dividir por zero!")

else:
    print("Operação inválida! Tente novamente.")
