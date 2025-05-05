# capitais

capitais = {
    'Brasil': 'Brasília',
    'França': 'Paris',
    'Japão': 'Tóquio',
    'Inglaterra': 'Londres'
}

for pais in capitais:
    capital = capitais[pais]
    print(f'A capital de {pais} é {capital}')


# dicionario vazio

d = dict()

d[10] = 'abc'
d['CHAVE'] = 5
d[3.15] = True

for k in d:
    v = d[k]
    print(f'Chave: {k}, Valor: {v}')


# O operador IN

capitais = {
    'Brasil': 'Brasília',
    'França': 'Paris',
    'Japão': 'Tóquio',
    'Inglaterra': 'Londres'
}

pais = 'Brasil'

if pais in capitais:
    capital = capitais[pais]
    print(f'A capital de {pais} é {capital}')
else:
    print(f'Não há capital registrada para o país {pais}!')


while True:
    opt = input('Escolha uma opção (1, 2) | ''q'' para sair: ')
    if opt == 'q':
        break
    elif opt not in ('1', '2'):
        print('Opção inválidade! Digite 1 ou 2.')
        continue
    else:
        print(f'Opção selecionada: {opt}')
