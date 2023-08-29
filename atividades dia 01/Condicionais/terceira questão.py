num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))

if(num1 > num2 and num1 > num3):
    maior_numero = num1
    print('Primeiro numero é o maior: ', maior_numero)
elif(num2 > num1 and num2 > num3):
    maior_numero = num2
    print('O segundo numero é o maior: ',maior_numero)
elif(num3 > num1 and num3 > num2):
    maior_numero = num3
    print('O terceiro numero é o maior: ',maior_numero)

if(num1 < num2 and num1 < num3):
    menor_numero = num1
    print('Primeiro numero é o menor: ', menor_numero)
elif(num2 < num1 and num2 < num3):
    menor_numero = num2
    print('O segundo numero é o menor: ',menor_numero)
elif(num3 > num1 and num3 > num2):
    menor_numero = num3
    print('O terceiro numero é o menor: ',menor_numero)
    