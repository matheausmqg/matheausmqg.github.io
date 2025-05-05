n = 0

while n < 3:
    print(f'O valor de n é: {n}')
    n = n + 1  # pode usar n += 1 (forma reduzida)

print('O Loop acabou!')


# BREAK E CONTINUE

n = 0

while n < 10:
    print(f'O valor de n é: {n}')
    n = n + 1  # pode usar n += 1 (forma reduzida)
    if n == 5:
        break

print('O Loop acabou!')

# CONTINUE

for n in range(-5, 6):
    print(n)
    if n == 0:
        continue
    resultado = 1 / n
    print(f'O resultado é: {resultado}')

print('O Loop acabou!')

# WHILE TRUE

while True:
    entrada = input('Digite qualquer coisa ("q" para sair): ')
    print(f'O valor digitado foi: {entrada}')
    if entrada == 'q':
        break
print('Programa finalizado!')

while True:
    opt = input('Escolha uma opção (1, 2) | ("q" para sair): ')
    if opt == 'q':
        break
    elif opt != '1' and opt != '2':
        print('Opção Inválida!')
        continue
    print(f'Opção selecionada: {opt}')

print('Programa finalizado!')
