"""
numero = 0
while numero <= 5:
    print("Número:", numero)
    numero += 1
 
coordenadas = (10, 20) #Tuple
print(coordenadas[0])  # Mostra 10

dias_da_semana = ("Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom")
print(dias_da_semana[2])

aluno = {"nome": "Ana", "idade": 17, "nota": 9.5} #dict
print(aluno["nome"])  # Mostra "Ana"

aluno["turma"] = "3A"    # Adiciona nova chave
aluno["nota"] = 10       # Atualiza valor
del aluno["idade"]       # Remove chave

print(aluno)

numeros = {1, 2, 3, 3, 2} #Set
print(numeros)  # Resultado: {1, 2, 3}

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)  # União: {1, 2, 3, 4, 5, 6}
print(A & B)  # Interseção: {3, 4}
print(B - A)  # Diferença: {1, 2}
"""
# Cadastro simples de alunos

alunos = []

while True:
    nome = input("Nome do aluno (ou 'sair'): ")
    if nome == 'sair':
        break
    idade = int(input("Idade: "))
    nota = float(input("Nota: "))

    aluno = {"nome": nome, "idade": idade, "nota": nota}
    alunos.append(aluno)

print("\n--- Lista de alunos ---")
for a in alunos:
    print(f"{a['nome']} - {a['idade']} anos - Nota: {a['nota']}")
