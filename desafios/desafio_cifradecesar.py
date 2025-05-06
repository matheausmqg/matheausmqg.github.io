# Crie um código que implementa a ''Cifra de César'', isto é, que transforma um string
# movendo cada letra um certo número de passos no alfabeto. O número de passos é dado
# por uma chave. Letra com acentos, espaços e pontuações permanecem iguais.

# Exemplos:
# "abc" com chave 1 = "bcd"
# "ABCDE" com chave 2 = "CDEFG"
# "Cachorro" com chave -1 = "Bzbgnqqn"

# DICA: construa 2 strings com as letras do alfabeto em ordem, um para letras
# maiúsculas e outra para as minúsculas, e use este string para guiar as substituições.


def cifra_de_cesar(texto, chave):
    alfabeto_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alfabeto_minusculas = 'abcdefghijklmnopqrstuvwxyz'
    resultado = ''

    for caractere in texto:
        if caractere in alfabeto_maiusculas:
            indice = alfabeto_maiusculas.index(caractere)
            novo_indice = (indice + chave) % 26
            resultado += alfabeto_maiusculas[novo_indice]
        elif caractere in alfabeto_minusculas:
            indice = alfabeto_minusculas.index(caractere)
            novo_indice = (indice + chave) % 26
            resultado += alfabeto_minusculas[novo_indice]
        else:
            resultado += caractere  # Mantém acentos, espaços, pontuação etc.

    return resultado


# Parte interativa
if __name__ == "__main__":
    texto_usuario = input("Digite o texto para cifrar: ")
    try:
        chave = int(
            input("Digite a chave (número de posições para deslocar): "))
        texto_cifrado = cifra_de_cesar(texto_usuario, chave)
        print("Texto cifrado:", texto_cifrado)
    except ValueError:
        print("Por favor, digite um número válido para a chave.")


# codigo curso

def cifrar_caractere(caractere, seq, chave):
    indice_atual = seq.index(caractere)
    novo_indice = indice_atual + chave
    while novo_indice >= len(seq):
        novo_indice = novo_indice - len(seq)
    while novo_indice < 0:
        novo_indice = novo_indice + len(seq)
    return seq[novo_indice]


texto = 'Estou aprendendo Python'
chave = 1

maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
minusculas = 'abcdefghijklmnopqrstuvwxyz'

cifra = ''

for caractere in texto:
    if caractere in minusculas:
        caractere_cifra = cifrar_caractere(caractere, minusculas, chave)
    elif caractere in maiusculas:
        caractere_cifra = cifrar_caractere(caractere, maiusculas, chave)
    else:
        caractere_cifra = caractere
    cifra += caractere_cifra

print(cifra)
