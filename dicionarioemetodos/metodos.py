# objetos próprios.

s = 'Olá Mundo!'

num = 10

dec = 3.33

lista = [1, 2, 3]

tupla = ('A', 'B', 'C')

dic = {'chave1': 'valor1', 'chave2': 'valor2'}


# Métodos (estão em todos os objetos)

# Métodos de dicionário

produtos = {
    'banana': 3.60,
    'leite': 4.90,
    'carne': 15.50
}

# metodo CLEAR = produtos.clear()   |   usado para eliminar dados de um objeto.
# metodo GET = produtos.get('banana')   |    usado para pegar um valor associado a uma chave.
# metodo SETDEFAULT = produtos.setdefault('banana')    |    igual GET, mas qnd chave nao existe ele coloca uma q voce escolhe
# metodo keys/values/items    |   servem para interar no dicionario de diferentes formas.
# metodo UPDATE |    atualizar um dicionario a partir de outro.
# metodo COPY    |    serve pra criar uma cópia independente do dicionarios.


# Métodos de Strings e Números
# Números
# x.as_integer_ratio()   |   razão de numeros inteiros (mostra 2 numeros que divididos da o x)
# x.is_integer()    |    pergunta se o numero é inteiro

# Strings
# metodo lower/upper    |    transforma tudo em maiusculo ou minusculo.
# metodo endswith    |    encontra/identifica como um arquivo termina a escrita.
# metodo startswith    |    encontra/identifica como um arquivo começa a escrita.
# pode misturar os 2 de cima
# metodo count    |    contar caracteres ou palavras em um string.
# metodo find/index    |    encontrar uma posição de um caractere em string.
# SE NÃO ACHAR = find retorna -1, index retorna um ERRO.
# metodo isdigit() = reconhece se tudo é numero.
# metodo isalpha() = reconhece se tudo é letra.
# metodo replace    |   trocar uma palavra/caractere por outro em determinada frase etc.
# metodo split    |    quebra espaços em branco .
# metodo join    |    intercala um string que voce quer alterar.


# Métodos de Tuplas e Listas.
# Tuplas
# metodo count    |    contar caracteres ou palavras em um string.
# metodo index    |    encontrar uma posição de um caractere em string.

# Listas
# metodo count    |    contar caracteres ou palavras em um string.
# metodo index    |    encontrar uma posição de um caractere em string.
# metodo copy     |    serve pra criar uma cópia independente da lista.
# metodo clear    |    usado para eliminar dados de uma lista.
# metodo append    |    colocar um elemento no final da lista.
# metodo extend    |    extende a lista anterior botando cada um dos valores.
# metodo insert    |    inserir valores numa lista.
# metodo pop     |    remover valores de dentro da lista.
# metodo reverse    |    inverte a lista
# metodo sort    |    ordena a lista do menor para o maior. *valores comparáveis.
