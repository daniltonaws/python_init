"""Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”. """

def eh_palindromo(texto: str) -> bool:
    # Remove espaços e pontuação, e converte para minúsculas
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
    # Verifica se o texto é igual ao seu reverso
    return texto_limpo == texto_limpo[::-1]
def main():
    print("=== Verificador de Palíndromos ===")
    while True:
        entrada = input("Digite uma palavra ou frase (ou 'sair' para encerrar): ").strip()
        
        if entrada.lower() == 'sair':
            print("Programa encerrado.")
            break
        
        if eh_palindromo(entrada):
            print("Sim")
        else:
            print("Não")
if __name__ == "__main__":
    main()
# Fim do programa