# None é um valor que representa ausencia de um valor, ou seja, ele é ALGO.

def dizer_ola():
    print('Olá!')


retorno = dizer_ola()
print(retorno)


produtos = {
    'banana': 3.60,
    'leite': 4.90,
    'carne': 15.50
}

print(produtos.get('Arroz'))
