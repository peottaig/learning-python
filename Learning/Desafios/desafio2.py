def saudaUsuario(hora):
    if hora >= 0 and hora <= 11:
        print("Bom dia")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde")
    elif hora >= 18 and hora <= 23:
        print("Boa noite")
    else:
        print("Dado invalido fornecido")


try:
    hora = int(input("Digite a hora atual: "))
    saudaUsuario(hora)
except:
    print("Dado invalido fornecido")
