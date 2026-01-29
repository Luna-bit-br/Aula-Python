# Calculadora 

def ler_numeros():
    while True:
        entrada = input("Digite os números (separados por espaço ou vírgula): ").strip()
        # aceita espaços ou vírgulas como separadores
        entrada = entrada.replace(",", " ")
        partes = [p for p in entrada.split() if p != ""]
        try:
            numeros = [float(p) for p in partes]
        except ValueError:
            print("Entrada inválida. Digite apenas números separados por espaço ou vírgula.")
            continue

        if len(numeros) < 2:
            print("Digite pelo menos 2 números.")
            continue

        return numeros

def calcular(operacao, numeros):
    if operacao == "+":
        return sum(numeros)

    elif operacao == "-":
        resultado = numeros[0]
        for n in numeros[1:]:
            resultado -= n
        return resultado

    elif operacao == "*":
        resultado = 1.0
        for n in numeros:
            resultado *= n
        return resultado

    elif operacao == "/":
        resultado = numeros[0]
        for n in numeros[1:]:
            if n == 0:
                # evita divisão por zero
                raise ZeroDivisionError("Divisão por zero detectada em um dos operandos.")
            resultado /= n
        return resultado

    else:
        raise ValueError("Operação inválida")

def main():
    print("=== Calculadora com N números ===")
    operacao = input("Escolha a operação (+, -, *, /): ").strip()

    numeros = ler_numeros()

    try:
        resultado = calcular(operacao, numeros)
    except ZeroDivisionError as zde:
        print("Erro:", zde)
        return
    except ValueError as ve:
        print("Erro:", ve)
        return

    print("Números:", numeros)
    print("Operação:", operacao)
    print("Resultado:", resultado)

if __name__ == "__main__":
    main()
