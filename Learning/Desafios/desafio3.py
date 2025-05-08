def mede_tamanho_do_nome(nome):
    getlen = len(nome)
    if getlen <= 4:
        print("Seu nome é curto")
    elif getlen >= 5 and getlen <= 6:
        print("Seu nome é normal")
    elif getlen > 6:
        print("Seu nome é muito grande")


try:
    nome = input("Insira seu nome: ")
    mede_tamanho_do_nome(nome)
except:
    print("Dado invalido")
