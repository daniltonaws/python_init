# Calculadora de Comissão

print("=== Calculadora de Comissão ===")

# Entrada dos dados
nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo: R$ "))
total_vendas = float(input("Digite o total de vendas no mês: R$ "))

# Cálculo da comissão
comissao = total_vendas * 0.15
salario_total = salario_fixo + comissao

# Saída formatada
print(f"\nVendedor: {nome}")
print(f"Salário fixo: R$ {salario_fixo:.2f}")
print(f"Comissão (15% sobre R$ {total_vendas:.2f}): R$ {comissao:.2f}")
print(f"Total a receber no final do mês: R$ {salario_total:.2f}")
