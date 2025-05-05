def somar_dois(n):
    return n + 2


x = 10                    # n = paramentro / x = argumento

resultado = somar_dois(x)

print(resultado)


def adicionar_final(texto, final="!!!"):
    return texto + final


print(adicionar_final('Olá'))

# funcao dividir


def dividir(a, b):
    if b == 0:
        return 'Impossível dividir!'
    return a / b


print(dividir(10, 2))
print(dividir(a=10, b=2))


def funcao_complexa(
    param_1=0,
    param_2=0,
    param_3=0
):
    return param_1 + param_2 + param_3


print(funcao_complexa(param_3=10))


def dizer_ola():
    print('Olá!')


dizer_ola()
dizer_ola()
dizer_ola()
