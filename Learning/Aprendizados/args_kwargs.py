def mostra_argumentos(*args, **kwargs):
    print(f"Args: {args}")
    for chave, valor in kwargs.items():
        print(f"Chave: {chave}")
        print(f"Valor: {valor}")


mostra_argumentos(nome="Lucas", sobrenome="Amaral")
