"""Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória."""

import random
def gerar_senha(tamanho: int) -> str:
    """Gera uma senha aleatória com o tamanho especificado."""
    caracteres = (
        "abcdefghijklmnopqrstuvwxyz"  # Letras minúsculas
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Letras maiúsculas
        "0123456789"                     # Dígitos
        "!@#$%^&*()-_=+[]{}|;:,.<>?/"   # Caracteres especiais
    )
    
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha
def main():
    print("=== Gerador de Senha Aleatória ===")
    while True:
        try:
            tamanho = int(input("Digite o tamanho da senha (ou '0' para encerrar): "))
            if tamanho == 0:
                print("Programa encerrado.")
                break
            
            if tamanho < 1:
                print("O tamanho da senha deve ser pelo menos 1. Tente novamente.")
                continue
            
            senha_gerada = gerar_senha(tamanho)
            print(f"Senha gerada: {senha_gerada}")
        
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
if __name__ == "__main__":
    main()
# Fim do programa