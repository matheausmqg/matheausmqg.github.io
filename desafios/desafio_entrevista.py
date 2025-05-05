# Desafio - crie um programa que:
# - Pede pelo seu nome e idade
# - Dá oi para você
# - Conta quantas letras seu nome possui
# - Fala quantos anos você terá daqui a 5 anos

print("Olá, aqui é seu assistente virtual!")
user = input("Qual o seu nome? ")
idade = int(input("Qual sua idade? "))
anos = (idade + 5)
print("Olá", user, "!")
print("Seu nome possui", len(user), "letras!")
print("Você sabia que daqui a 5 anos você terá", anos, "anos!")

# FORMATAÇÃO USADA

nome = input('Qual o seu nome? ')
idade = input('Qual sua idade? ')

print(f'Olá, {nome}!')
print(f'Seu nome tem {len(nome)} letras.')
print(f'Daqui 5 anos, você terá {int(idade) + 5} anos.')
