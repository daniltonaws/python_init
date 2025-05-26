"""5- Calculadora de Soma com Entrada do Usuário

Leia 2 valores inteiros e armazene-os nas variáveis A e B. Efetue a soma de A e B, atribuindo o seu resultado à variável X. Entrada: A entrada contém 2 valores inteiros informados pelo usuário. Saída:

Imprima a mensagem "X = " (letra X maiúscula) seguido pelo valor da variável X e pelo final de linha."""

# Lendo os valores inteiros A e B
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
# Efetuando a soma
X = A + B
# Imprimindo o resultado
print(f"X = {X}")