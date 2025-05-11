import json
CAMINHO_AQUIVO = r"C:\\Users\\luigg\\learning-python\\Learning\\Dados\\classPessoa.json"


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa("Luggi", 18)
p2 = Pessoa("Gabriel", 15)
p3 = Pessoa("Sergio", 23)

dados = [vars(p1), vars(p2), vars(p3)]

with open(CAMINHO_AQUIVO, "w") as arquivo:
    json.dump(dados, arquivo)
