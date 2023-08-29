numero = int(input("Digite um numero de 0 a 10 para aparece a taboada de soma: "))

for i in range(11):
    resultado = numero + i
    print(f"{numero} + {i} = {resultado}")