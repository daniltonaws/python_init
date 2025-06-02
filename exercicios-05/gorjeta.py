"""Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

Parâmetros: valor_conta (float): O valor total da conta porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)

Retorna: float: O valor da gorjeta calculada
"""

def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    return valor_conta * (porcentagem_gorjeta / 100)
def main():
    print("=== Calculadora de Gorjeta ===")
    while True:
        try:
            valor_conta = float(input("Digite o valor total da conta (ou '0' para encerrar): "))
            if valor_conta == 0:
                print("Programa encerrado.")
                break
            
            porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta (ex: 15 para 15%): "))
            if porcentagem_gorjeta < 0:
                print("Porcentagem inválida. Deve ser um número positivo.")
                continue
            
            gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
            print(f"A gorjeta a ser deixada é: R$ {gorjeta:.2f}")
        
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
if __name__ == "__main__":
    main()
# Fim do programa