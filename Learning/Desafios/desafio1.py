def verificaIpopar(numero):
    if numero % 2 == 0:
        print("O numero é par")
    else:
        print("O numero é impar")


try:
    numero = int(input("Digite um numero: "))
    verificaIpopar(numero)
except:
    print("O caracter digitado não é valido")
