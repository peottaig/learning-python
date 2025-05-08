# Operadores uteis:
# União | união - une
# Intersecção & - Itens presentes em ambos
# Diferença - Itens presentes apenas np set da esquerda
# Diferencça simetrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3, 3, 3, 3, 3}
s2 = {3, 4, 5}

s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2
s3 = s1 ^ s2

# print(s3)

# Metodos Uteis
# add, update, clear, discard
discard = "Luiz"
s1 = set()
s1.add("Luiz")
s1.add(1)
s1.update(("Olá pessoal", 1, 2, "Teste"))
# s1.clear()
s1.discard(discard)

print(s1)
