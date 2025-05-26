"""4- Conversor de Temperatura Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter."""

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_para_kelvin(c):
    return c + 273.15

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_para_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_para_celsius(k):
    return k - 273.15

def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def converter_temperatura(valor, origem, destino):
    if origem == destino:
        return valor

    if origem == 1:  # Celsius
        if destino == 2:
            return celsius_para_fahrenheit(valor)
        elif destino == 3:
            return celsius_para_kelvin(valor)

    elif origem == 2:  # Fahrenheit
        if destino == 1:
            return fahrenheit_para_celsius(valor)
        elif destino == 3:
            return fahrenheit_para_kelvin(valor)

    elif origem == 3:  # Kelvin
        if destino == 1:
            return kelvin_para_celsius(valor)
        elif destino == 2:
            return kelvin_para_fahrenheit(valor)

    return None

def nome_unidade(opcao):
    if opcao == 1:
        return "Celsius"
    elif opcao == 2:
        return "Fahrenheit"
    elif opcao == 3:
        return "Kelvin"

# Programa principal
print("=== Conversor de Temperatura ===")
print("Escolha a unidade de origem:")
print("1 - Celsius")
print("2 - Fahrenheit")
print("3 - Kelvin")
origem = int(input("Digite o número da unidade de origem: "))

print("\nEscolha a unidade de destino:")
print("1 - Celsius")
print("2 - Fahrenheit")
print("3 - Kelvin")
destino = int(input("Digite o número da unidade de destino: "))

valor = float(input("\nDigite o valor da temperatura: "))

resultado = converter_temperatura(valor, origem, destino)

if resultado is not None:
    print(f"\n{valor:.2f} {nome_unidade(origem)} é igual a {resultado:.2f} {nome_unidade(destino)}.")
else:
    print("Conversão inválida. Verifique as opções selecionadas.")
