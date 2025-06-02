"""Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação."""

import requests

def consultar_cotacao(moeda: str):
    """Consulta a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL)."""
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if f"{moeda}BRL" in data:
            cotacao = data[f"{moeda}BRL"]
            return {
                "valor": cotacao["bid"],
                "maximo": cotacao["high"],
                "minimo": cotacao["low"],
                "data_hora": cotacao["create_date"]
            }
        else:
            raise ValueError("Moeda não encontrada.")
    else:
        raise Exception("Erro ao acessar a API.")

def main():
    print("=== Consultor de Cotação de Moeda ===")
    while True:
        moeda = input("Digite o código da moeda (ex: USD, EUR, GBP) ou 'sair' para encerrar: ").strip().upper()
        
        if moeda.lower() == 'sair':
            print("Programa encerrado.")
            break
        
        try:
            cotacao = consultar_cotacao(moeda)
            print(f"Cotação de {moeda} em relação ao BRL:")
            print(f"Valor atual: R$ {float(cotacao['valor']):.2f}")
            print(f"Máximo: R$ {float(cotacao['maximo']):.2f}")
            print(f"Mínimo: R$ {float(cotacao['minimo']):.2f}")
            print(f"Data e hora da última atualização: {cotacao['data_hora']}")
        except ValueError as ve:
            print(f"Erro: {ve}")
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()
# Fim do programa