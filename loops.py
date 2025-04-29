# Loops (repetir ações/coisas etc)

for n in range(5):
    print(f'O valor de n é: {n}')

for n in range(5):
    print('Olá Mundo!!')


numero_secreto = 10
descobriu = False

for n in range(3):
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
