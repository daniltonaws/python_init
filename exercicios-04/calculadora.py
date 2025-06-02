"""Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração, multiplicação e divisão) entre dois números. A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. Siga as especificações abaixo:



A calculadora deve solicitar ao usuário que insira dois números e uma operação.

As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).

O programa deve continuar solicitando entradas até que uma operação válida seja concluída.

Trate os seguintes erros:

Entrada inválida (não numérica) para os números

Divisão por zero

Operação inválida



Use try/except para capturar e tratar os erros apropriadamente.

Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.

Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa."""

while True:
    print("=== Calculadora Simples ===")
    print("Quer caucular algo? (s/n)")
    resposta = input("Digite 's' para sim ou 'n' para não: ").strip().lower()
    if resposta == 'n':
        print("Programa encerrado.")
        break
    elif resposta != 's':
        print("Opção inválida. Por favor, digite 's' ou 'n'.")
        continue
    print("Você escolheu calcular.")

    def calculadora():
        while True:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                operacao = input("Digite a operação (+, -, *, /): ")

                if operacao == '+':
                    resultado = num1 + num2
                elif operacao == '-':
                    resultado = num1 - num2
                elif operacao == '*':
                    resultado = num1 * num2
                elif operacao == '/':
                    if num2 == 0:
                        raise ZeroDivisionError("Divisão por zero não é permitida.")
                    resultado = num1 / num2
                else:
                    raise ValueError("Operação inválida. Use +, -, * ou /.")

                print(f"Resultado: {resultado}")
                break  # Encerra o loop após uma operação bem-sucedida

            except ValueError as ve:
                print(f"Erro de entrada: {ve}. Tente novamente.")
            except ZeroDivisionError as zde:
                print(f"Erro: {zde}. Tente novamente.")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}. Tente novamente.")
    if __name__ == "__main__":
        calculadora()