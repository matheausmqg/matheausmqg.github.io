# Dado duas listas, printe todos os valores que aparecem
# duplicados nas duas listas.

valores1 = [10, 20, 30, 40, 50]
valores2 = [21, 27, 30, 35, 50, 52, 58]

for valor1 in valores1:
    for valor2 in valores2:
        if valor1 == valor2:
            print(f'Valor {valor1} aparece nas duas listas')


# Dado duas lista, printe uma mensagem dizendo se existe
# algum elemento em comum entres elas ou não.

lista1 = [10.0, 'xx', True]
lista2 = [0, False, 'xx']

elemento_em_comum = False

for valor1 in lista1:
    for valor2 in lista2:
        if valor1 == valor2:
            elemento_em_comum = True
if elemento_em_comum:
    print(f'As listas {lista1} e {lista2} possuem elementos em comum!')
else:
    print(f'As listas {lista1} e {lista2} não possuem elementos em comum1')
