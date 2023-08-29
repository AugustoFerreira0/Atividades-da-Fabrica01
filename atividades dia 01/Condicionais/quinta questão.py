nomes_validos = ["João Maia", "João Abrantes", "Pedro"]

nome = input("Digite um nome: ")


if nome in nomes_validos:
    print(f"Oi, eu sou {nome.lower()}")
else:
    print(f"Oi, meu nome é {nome}")
