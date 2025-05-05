# Neste jogo, o jogador precisa responder o nome da capital de cada Estado do Brasil
# O jogo deve perguntar ao usuário ''Qual a capital do Estado X?'', e checar se o usuário
# responder de forma correta. Após cada perguntam, o usuário pode escolher parar o jogo ou
# continuar para a próxima pergunta. Quando o usuário decidir parar, ou quando todas as perguntas
# forem respondidas, o código mostra o número bruto e porcentagem de acertos.

import random

estados_capitais = {
    "Acre": "Rio Branco",
    "Alagoas": "Maceió",
    "Amapá": "Macapá",
    "Amazonas": "Manaus",
    "Bahia": "Salvador",
    "Ceará": "Fortaleza",
    "Distrito Federal": "Brasília",
    "Espírito Santo": "Vitória",
    "Goiás": "Goiânia",
    "Maranhão": "São Luís",
    "Mato Grosso": "Cuiabá",
    "Mato Grosso do Sul": "Campo Grande",
    "Minas Gerais": "Belo Horizonte",
    "Pará": "Belém",
    "Paraíba": "João Pessoa",
    "Paraná": "Curitiba",
    "Pernambuco": "Recife",
    "Piauí": "Teresina",
    "Rio de Janeiro": "Rio de Janeiro",
    "Rio Grande do Norte": "Natal",
    "Rio Grande do Sul": "Porto Alegre",
    "Rondônia": "Porto Velho",
    "Roraima": "Boa Vista",
    "Santa Catarina": "Florianópolis",
    "São Paulo": "São Paulo",
    "Sergipe": "Aracaju",
    "Tocantins": "Palmas"
}


def jogar_quiz():
    estados = list(estados_capitais.keys())
    random.shuffle(estados)  # Embaralha a ordem das perguntas
    acertos = 0
    total_perguntas = 0

    for estado in estados:
        resposta = input(f"Qual a capital do Estado {estado}? ").strip()

        if resposta.lower() == estados_capitais[estado].lower():
            print("Resposta correta!\n")
            acertos += 1
        else:
            print(
                f"Errado. A capital de {estado} é {estados_capitais[estado]}.\n")

        total_perguntas += 1

        continuar = input("Deseja continuar? (s/n): ").strip().lower()
        if continuar != 's':
            break

    print("\nJogo encerrado.")
    print(f"Você acertou {acertos} de {total_perguntas} perguntas.")
    if total_perguntas > 0:
        porcentagem = (acertos / total_perguntas) * 100
        print(f"Porcentagem de acertos: {porcentagem:.2f}%")


# Inicia o jogo
jogar_quiz()


# Exemplo CURSO

estados_e_capitais = {
    "Acre": "Rio Branco",
    "Alagoas": "Maceió",
    "Amapá": "Macapá",
    "Amazonas": "Manaus",
    "Bahia": "Salvador",
    "Ceará": "Fortaleza",
    "Distrito Federal": "Brasília",
    "Espírito Santo": "Vitória",
    "Goiás": "Goiânia",
    "Maranhão": "São Luís",
    "Mato Grosso": "Cuiabá",
    "Mato Grosso do Sul": "Campo Grande",
    "Minas Gerais": "Belo Horizonte",
    "Pará": "Belém",
    "Paraíba": "João Pessoa",
    "Paraná": "Curitiba",
    "Pernambuco": "Recife",
    "Piauí": "Teresina",
    "Rio de Janeiro": "Rio de Janeiro",
    "Rio Grande do Norte": "Natal",
    "Rio Grande do Sul": "Porto Alegre",
    "Rondônia": "Porto Velho",
    "Roraima": "Boa Vista",
    "Santa Catarina": "Florianópolis",
    "São Paulo": "São Paulo",
    "Sergipe": "Aracaju",
    "Tocantins": "Palmas"
}

quer_continuar = True
rodadas = 0
acertos = 0


for estado, capital in estados_e_capitais.items():
    if not quer_continuar:
        break

    rodadas += 1
    print(f'\n -> Qual a capital do estado {estado}?')

    resposta = input('Sua resposta: ')
    if resposta.lower() == capital.lower:
        print('Resposta correta!')
        acertos += 1
    else:
        print(f'Resposta errada! O correto seria {capital}')

    while True:
        opcao = input('Deseja continuar? (s/n)').lower()
        if opcao not in ['s', 'n']:
            print('Responda apenas com ''s'' para sim ou ''n'' para não.')
            continue
        elif opcao == 'n':
            quer_continuar = False
        break

porc = acertos / rodadas * 100

print(f'VocÊ acertou {acertos} de {rodadas}')
print(f'Porcetagem de acertos: {porc:.2f%}')
