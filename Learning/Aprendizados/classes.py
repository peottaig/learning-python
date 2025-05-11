# import json
# CAMINHO_AQUIVO = r"C:\\Users\\luigg\\learning-python\\Learning\\Dados\\classPessoa.json"


# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade


# with open(CAMINHO_AQUIVO, "r") as arquivo:
#     dados = json.load(arquivo)


# p1 = Pessoa(**dados[0])
# p2 = Pessoa(**dados[1])
# p3 = Pessoa(**dados[2])

# print(p1.nome, p1.idade)
# print(p2.nome, p2.idade)
# print(p3.nome, p3.idade)

# class Cores:

#     def __init__(self, cor):
#         self._cor = cor

#     @property
#     def cor(self):
#         return self._cor

#     @cor.setter
#     def cor(self, valor):
#         print("setter")
#         if not isinstance(valor, str):
#             raise ValueError("Não é string")
#         self._cor = valor


# caneta = Cores("Verde")
# caneta.cor = "Amarelo"
# print(caneta.cor)

# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).
class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])

    def inserir_produtos(self, *produtos):
        # self._produtos.extend(produtos)
        # self._produtos += produtos
        for produto in produtos:
            self._produtos.append(produto)

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())
