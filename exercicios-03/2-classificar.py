"""2- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o em uma das seguintes categorias:

Criança (0-12 anos),

Adolescente (13-17 anos),

Adulto (18-59 anos)

Idoso (60 anos ou mais)."""

# Solicita a idade do usuário
idade = int(input("Digite a sua idade: "))
# Classifica a idade em categorias
if idade >= 0 and idade <= 12:
    categoria = "Criança"
elif idade >= 13 and idade <= 17:
    categoria = "Adolescente"
elif idade >= 18 and idade <= 59:
    categoria = "Adulto"
elif idade >= 60:
    categoria = "Idoso"
else:
    categoria = "Idade inválida"
# Exibe a categoria correspondente
print(f"Você é classificado como: {categoria}")