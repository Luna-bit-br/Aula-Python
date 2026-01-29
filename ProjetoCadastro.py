# =====================================================
# CADASTRO DE PESSOAS - BANCO DE DADOS SIMPLES EM PYTHON
# =====================================================
# Este programa permite:
# - Cadastrar pessoas
# - Salvar nome, idade e profissão
# - Listar todas as pessoas cadastradas
# =====================================================


# -----------------------------------------------------
# 1) CRIAÇÃO DO "BANCO DE DADOS"
# -----------------------------------------------------
# Aqui usamos uma LISTA para armazenar várias pessoas.
# Cada pessoa será um DICIONÁRIO.
banco_de_dados = []


# -----------------------------------------------------
# 2) LOOP PRINCIPAL DO PROGRAMA
# -----------------------------------------------------
# O while True mantém o programa rodando até o usuário sair
while True:

    print("\n===== MENU =====")
    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas cadastradas")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")


    # -------------------------------------------------
    # 3) OPÇÃO 1 - CADASTRAR PESSOA
    # -------------------------------------------------
    if opcao == "1":

        # Entrada de dados do usuário
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        profissao = input("Digite a profissão: ")

        # Criamos um DICIONÁRIO para representar uma pessoa
        pessoa = {
            "nome": nome,
            "idade": idade,
            "profissao": profissao
        }

        # Adicionamos a pessoa ao banco de dados
        banco_de_dados.append(pessoa)

        print("Pessoa cadastrada com sucesso!")


    # -------------------------------------------------
    # 4) OPÇÃO 2 - LISTAR PESSOAS
    # -------------------------------------------------
    elif opcao == "2":

        # Verifica se o banco está vazio
        if len(banco_de_dados) == 0:
            print("Nenhuma pessoa cadastrada.")
        else:
            print("\n--- PESSOAS CADASTRADAS ---")

            # Percorre a lista de pessoas
            for i, pessoa in enumerate(banco_de_dados, start=1):
                print(f"\nPessoa {i}")
                print("Nome:", pessoa["nome"])
                print("Idade:", pessoa["idade"])
                print("Profissão:", pessoa["profissao"])


    # -------------------------------------------------
    # 5) OPÇÃO 3 - SAIR DO PROGRAMA
    # -------------------------------------------------
    elif opcao == "3":
        print("Encerrando o programa...")
        break


    # -------------------------------------------------
    # 6) OPÇÃO INVÁLIDA
    # -------------------------------------------------
    else:
        print("Opção inválida. Tente novamente.")
