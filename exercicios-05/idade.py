"""Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento."""

def calcular_idade_em_dias(ano_nascimento: int, mes_nascimento: int, dia_nascimento: int) -> int:
    from datetime import datetime
    
    # Data atual
    data_atual = datetime.now()
    
    # Data de nascimento
    data_nascimento = datetime(ano_nascimento, mes_nascimento, dia_nascimento)
    
    # Calcula a diferença em dias
    idade_em_dias = (data_atual - data_nascimento).days
    
    return idade_em_dias
def main():
    print("=== Calculadora de Idade em Dias ===")
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento (ou '0' para encerrar): "))
            if ano_nascimento == 0:
                print("Programa encerrado.")
                break
            
            mes_nascimento = int(input("Digite o mês de nascimento (1-12): "))
            dia_nascimento = int(input("Digite o dia de nascimento (1-31): "))
            
            idade_em_dias = calcular_idade_em_dias(ano_nascimento, mes_nascimento, dia_nascimento)
            print(f"A idade em dias é: {idade_em_dias} dias")
        
        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")
if __name__ == "__main__":
    main()
# Fim do programa