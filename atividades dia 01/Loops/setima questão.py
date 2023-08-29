qtde_macho = 0
qtde_mulheres = 0
sexo = ''

while(sexo != "sair"):
    sexo = input("Digite F para mulher, M para homem ou escreva sair para fechar o codigo: ")

    if(sexo == "F"):
        qtde_mulheres += 1
    elif(sexo == "M"):
        qtde_macho += 1
    else:
        print("Digite apenas F ou M!")
        
print(f"A quantidade final de mulheres foi: {qtde_mulheres}")
print(f"A quantidade final de homens foi: {qtde_macho}")
