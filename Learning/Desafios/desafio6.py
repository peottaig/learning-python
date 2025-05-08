"""
Quizzs usando dicionarios. praticando manipulação de itens de dicionarios
"""
# declarando variaveis
perguntas = [
    {
        "Pergunta": "Quanto é 2+2?",
        "Opções": ["1", "3", "4", "5"],
        "Resposta": "4",
    },
    {
        "Pergunta": "Quanto é 5*5?",
        "Opções": ["25", "55", "10", "51"],
        "Resposta": "25",
    },
    {
        "Pergunta": "Quanto é 10/2?",
        "Opções": ["4", "5", "2", "1"],
        "Resposta": "4",
    },
]
acertos = 0
entradaUser = ""
alternativas = 0
questao = 0

while True:
    print(f"Pergunta: {perguntas[questao]['Pergunta']}\n")
    print("Opções:")
    for itens in perguntas[questao]["Opções"]:
        print(f"{alternativas}) {itens}")
        alternativas += 1
    alternativas = 0

    entradaUser = str(input("Escolha uma opção: "))

    for itens in perguntas[questao]["Opções"]:
        if entradaUser == str(alternativas):
            entradaUser = itens
            if entradaUser == perguntas[questao]["Resposta"]:
                print("Acertou\n")
                acertos += 1
                break
            else:
                print("Errou\n")
                break
        alternativas += 1
    alternativas = 0

    questao += 1
    if questao == 3:
        print(f"Você acertou {acertos}\n de 3 perguntas")
        break
