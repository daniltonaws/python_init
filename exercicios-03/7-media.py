# Calculadora da Média com Exame

# Entrada das quatro notas
print("=== Calculadora da Média ===")
n1 = float(input("Digite a nota N1: "))
n2 = float(input("Digite a nota N2: "))
n3 = float(input("Digite a nota N3: "))
n4 = float(input("Digite a nota N4: "))

# Cálculo da média ponderada
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10
print(f"Media: {media:.1f}")

# Verificação da situação do aluno
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = float(input("Digite a nota do exame: "))
    print(f"Nota do exame: {nota_exame:.1f}")
    
    media_final = (media + nota_exame) / 2

    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    print(f"Media final: {media_final:.1f}")
