"""Calculadora de Média Escolar Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

Nota 1: 7.5
Nota 2: 8.0
Nota 3: 6.5 O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais."""

# Definindo as notas
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5
# Calculando a média
media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Resultado: Aprovado")
elif media >= 5:
    print("Resultado: Recuperação")
else:
    print("Resultado: Reprovado")

# Exibindo o resultado final
print(f"Resultado final: {media:.2f}")