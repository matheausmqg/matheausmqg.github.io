# Crie um código que conta o número de vogais de um bloco de texto qualquer
# O código deve desconsiderar letras maiúsculas/minusculas, A e a contam igual.
# O teto pode ser colocado diretamento como um string no código.

texto = '''
Nessa mesma expedição uma tempestade no Atlântico Sul provocou a perda de sete navios; as seis embarcações restantes encontraram-se eventualmente no Canal de Moçambique antes de prosseguirem para Calecute, na Índia. Cabral inicialmente obteve sucesso na negociação dos direitos de comercialização das especiarias, mas os comerciantes árabes consideraram o negócio português como uma ameaça ao monopólio deles e provocaram um ataque de muçulmanos e hindus ao entreposto português. Os portugueses sofreram várias baixas e suas instalações foram destruídas.
'''
vogais = {
    'A': 0,
    'E': 0,
    'I': 0,
    'O': 0,
    'U': 0,
}

for caractere in texto:
    if caractere.upper() == 'A':
        vogais['A'] += 1
    if caractere.upper() == 'E':
        vogais['E'] += 1
    if caractere.upper() == 'I':
        vogais['I'] += 1
    if caractere.upper() == 'O':
        vogais['O'] += 1
    if caractere.upper() == 'U':
        vogais['U'] += 1

for vogal, contagem in vogais.items():
    print(f'Há {contagem} letras {vogal} no texto.')


# exemplo 2

vogais = ["a", "e", "i", "o", "u"]
n_vogais = 0

texto_min = texto.lower()

for vogal in vogais:
    n_vogais = n_vogais + texto_min.count(vogal)
    print(f"O texto contém {texto_min.count(vogal)} vogais {vogal}.")

print(f"O número de vogais no texto é: {n_vogais}.")
