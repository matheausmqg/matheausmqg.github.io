# Desafio - crie um programa que:
# - Escolhe um número secreto.
# - Pede por um chute do usuário.
# - Indica se o usuário acertou ou não.
# - Se não acertou, dá uma dica dizendo se é maior ou menor
# - Repete isso até 3x!

numero_secreto = 10
descobriu = False

if not descobriu:
    chute = int(input('Descubra o número!\nSeu chute: '))
    if chute < numero_secreto:
        print('Chute muito baixo!')
    elif chute > numero_secreto:
        print('Chute muito alto!')
    else:
        print('Descobriu!')
        descobriu = True

if not descobriu:
    chute = int(input('Descubra o número!\nSeu chute: '))
    if chute < numero_secreto:
        print('Chute muito baixo!')
    elif chute > numero_secreto:
        print('Chute muito alto!')
    else:
        print('Descobriu!')
        descobriu = True

if not descobriu:
    chute = int(input('Descubra o número!\nSeu chute: '))
    if chute < numero_secreto:
        print('Chute muito baixo!')
    elif chute > numero_secreto:
        print('Chute muito alto!')
    else:
        print('Descobriu!')
        descobriu = True

if descobriu:
    print('Parabéns, você ganhou!')
else:
    print(f'Que pena, você perdeu! O número secreto era {numero_secreto}')
