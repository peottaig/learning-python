"""Calcula CPF"""
# Delcarando Variaveis
cpf = None  # 74682489070
multi = 10
multi2 = 11
soma = 0
soma2 = 0
resulD1 = None
verificaD1 = None
verificaD2 = None
digitosCal = None

# Pega CPF
cpf = input("Insira seu CPF: ")
digitos = cpf[-2:]

# Inicia os calculos para a validação do primerio digito
for numero in cpf:
    numero = int(numero)
    soma += numero * multi
    multi -= 1
    if multi == 1:
        resulD1 = (soma * 10) % 11
        break

verificaD1 = resulD1 if resulD1 <= 9 else 0

# Inicia os calculos para a validação do segundo digito
for numero in cpf:
    numero = int(numero)
    soma2 += numero * multi2
    multi2 -= 1
    if multi2 == 1:
        resulD1 = (soma2 * 10) % 11
        break

verificaD2 = resulD1 if resulD1 <= 9 else 0
digitosCal = str(verificaD1) + str(verificaD2)

print(f"o primeiro e segundo digitos são {verificaD1};{verificaD2}")
print(f"O cpf é valido" if digitos == digitosCal else f"O Cpf não é valido")
