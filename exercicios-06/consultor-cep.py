"""Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado."""

import requests
def consultar_cep(cep: str) -> dict:
    """Consulta informações de endereço a partir de um CEP usando a API ViaCEP."""
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Erro ao acessar a API ViaCEP.")
def main():
    print("=== Consultor de CEP ===")
    while True:
        cep = input("Digite o CEP (ou 'sair' para encerrar): ").strip()
        
        if cep.lower() == 'sair':
            print("Programa encerrado.")
            break
        
        if not cep.isdigit() or len(cep) != 8:
            print("CEP inválido. O CEP deve conter 8 dígitos. Tente novamente.")
            continue
        
        try:
            endereco = consultar_cep(cep)
            if 'erro' in endereco:
                print("CEP não encontrado. Tente novamente.")
            else:
                print(f"Logradouro: {endereco['logradouro']}")
                print(f"Bairro: {endereco['bairro']}")
                print(f"Cidade: {endereco['localidade']}")
                print(f"Estado: {endereco['uf']}")
        except Exception as e:
            print(f"Erro: {e}")
if __name__ == "__main__":
    main()
# Fim do programa