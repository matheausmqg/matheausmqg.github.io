idade = int(input('Digite sua idade: '))

if idade < 18:
    print('Você é menor de idade!')
    print('Por isso você não pode dirigir um carro.')
else:
    print('Você é maior de idade!')

# usa elif (condições específicas)
idade = int(input('Digite sua idade: '))

if idade < 18:
    print('Você tem menor de 18 anos!')
    print('Por isso você não pode dirigir um carro.')
elif idade == 18:
    print('Você tem exatamente 18 anos.')
else:
    print('Você tem mais de 18 anos!')
