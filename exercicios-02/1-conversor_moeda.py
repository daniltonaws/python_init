""""Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:
- Valor em reais: R$ 100.00
- Taxa do dólar: R$ 5.70
- Taxa do euro: R$ 6.40
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais."""

# Conversão de Reais para Dólares e Euros
# Definindo as taxas de conversão
valor_em_reais = float(input("Digite o valor em reais: "))
taxa_dolar = float(input("Digite a taxa de conversão do dólar: "))
taxa_euro = float(input("Digite a taxa de conversão do euro: "))

# Calculando o valor em dólares e euros
valor_em_euros = valor_em_reais / taxa_euro
valor_em_dolares = valor_em_reais / taxa_dolar

# Exibindo os resultados
print(f"O valor em reais é: {valor_em_reais:.2f}")
print(f"O valor em euros é: {valor_em_euros:.2f}")
print(f"O valor em dólares é: {round(valor_em_dolares, 2)}")