"""    3. Crie um programa que receba o preço original de um produto e um percentual de desconto, realizando o cálculo do preço final após a aplicação do desconto. Requisitos: 
        ◦ Permitir que o usuário informe o preço do produto e o percentual de desconto. 
        ◦ Utilizar operações matemáticas para calcular o valor do desconto e o preço final. 
        ◦ Exibir o preço final com duas casas decimais para garantir precisão. Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10). """

def calcular_desconto(preco_original: float, percentual_desconto: float) -> float:
    """Calcula o preço final após aplicar o desconto."""
    desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - desconto
    return preco_final
def main():
    print("=== Calculadora de Desconto ===")
    while True:
        try:
            preco_original = float(input("Digite o preço original do produto (ou '0' para encerrar): "))
            if preco_original == 0:
                print("Programa encerrado.")
                break
            
            percentual_desconto = float(input("Digite o percentual de desconto (ex: 10 para 10%): "))
            if percentual_desconto < 0:
                print("Percentual inválido. Deve ser um número positivo.")
                continue
            
            preco_final = calcular_desconto(preco_original, percentual_desconto)
            print(f"O preço final após o desconto é: R$ {preco_final:.2f}")
            print(f"Desconto aplicado: R$ {preco_original - preco_final:.2f}")
            print(f"Percentual de desconto: {percentual_desconto}%")
        
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
if __name__ == "__main__":
    main()
# Fim do programa