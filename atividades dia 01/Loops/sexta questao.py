soma = 0
numero = int(input("Digite um numero: "))

while(numero != 0):
    soma += numero
    numero = int(input("Digite um numero: "))

print(f"A soma de todos os numeros digitados foi: {soma}")  