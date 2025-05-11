import json
CAMINHO_AQUIVO = r"C:\\Users\\luigg\\learning-python\\Learning\\Dados\\classPessoa.json"


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


with open(CAMINHO_AQUIVO, "r") as arquivo:
    dados = json.load(arquivo)


# p1 = Pessoa(**dados[0])
# p2 = Pessoa(**dados[1])
# p3 = Pessoa(**dados[2])

# print(p1.nome, p1.idade)
# print(p2.nome, p2.idade)
# print(p3.nome, p3.idade)
