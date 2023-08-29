velopermi = 80
valor_multa = 7

veloCarro = int(input('Digite a velocidade do carro: '))

if(veloCarro > velopermi):
    velocidade_acima = veloCarro - velopermi
    multa_final = valor_multa * velocidade_acima 
    print('O valor da multa que você precisa pagar é de: ', multa_final)
else:
    print('Você não precisa pagar multa. Muito bem!')