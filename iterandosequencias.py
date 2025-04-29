valores = [10, 20, 30, 3, -2, 17]

for valor in valores:
    print(f'O valor é: {valor}')

print('Acabou o loop!')


# EXEMPLO STRING

nome = 'Juliano'

for caractere in nome:
    print(f'O caractere é: {caractere}')

print('Acabou o loop!')

# EXEMPLO LISTA c/ tuplas dentro

clientes = [
    ('Ana', 'xxx', 'xxx@gmail.com'),
    ('João', 'yyy', 'yyy@gmail.com')
]

for nome, cpf, email in clientes:
    print(f'Cliente: {nome}\nCPF: {cpf}\nEmail: {email}\n\n')

print('Acabou o loop!')
