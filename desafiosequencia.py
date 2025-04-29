# Dado uma sequencia de números, calcule a soma e média dos números.
# Atenção: não vale usar a função sum () !

valores = [10, 50, -9, 5, 33, 80]

soma = 0
for valor in valores:
    soma += valor

media = soma / len(valores)

print(f'A soma dos valores {valores} é: {soma}')
print(f'A média dos valores {valores} é: {media}')
print(sum(valores))  # usando sum()

print('\n\n')

# Dado uma sequencia de números, calcule o maior valor da sequencia.
# Atenção: não vale usar a função max() !

valores = [10, 50, -9, 5, 33, 80]

maximo = valores[0]
for valor in valores:
    if valor > maximo:
        maximo = valor

print(f'O valor máximo dos valores {valores} é: {maximo}')

print('\n\n')

# Dado ua lista de palavras, printe todas as palavras
# com pelo menso 5 caracteres.

palavras = ['Jumento', 'Lindo', 'Cão', 'liberdade', 'oi']
for palavra in palavras:
    if len(palavra) >= 5:
        print(f'Encontrada palavra com 5+ caracteres: {palavra}')
