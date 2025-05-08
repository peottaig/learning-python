import random as rd


def adivinhacao():
    secretWords = ["Abacaxi", "Maça", "Melancia", "Pera", "Caracol"]
    palavra_secreta = secretWords[rd.randint(0, len(secretWords) - 1)].lower()
    secret = "_" * len(palavra_secreta)

    print("Bem-vindo ao jogo de adivinhação!\n", 67 * "*", "\n")

    while secret != palavra_secreta:
        print(f"|{secret.capitalize()}|")
        palavra = input("Insira sua palavra ou chute: ").lower()

        if palavra in palavra_secreta:
            print(f"A palavra '{palavra}' está na palavra secreta!")
            # Encontra posição da substring
            pos = palavra_secreta.find(palavra)
            secret = secret[:pos] + palavra + \
                secret[pos+len(palavra):]  # Substitui diretamente

    print(f"Parabéns! A palavra secreta era '{palavra_secreta}'.")


adivinhacao()
