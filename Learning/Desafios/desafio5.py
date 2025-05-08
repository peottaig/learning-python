def lista_enu():
    lista = ["Vitor", "Amaral", "Ale", "Moises"]
    i = 0
    for intem in lista:
        print(f"{i} {intem}")
        i += 1


lista = ["Vitor", "Amaral", "Ale", "Moises"]
lista_enumerada = enumerate(lista)

for intem in lista_enumerada:
    print(intem)
