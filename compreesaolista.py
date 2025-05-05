valores = list(range(10))

maiores_que_cinco = []
for valor in valores:
    if valor > 5:
        maiores_que_cinco.append(valor)

# expressao equivalente ao que está acima
maiores_que_cinco = [valor for valor in valores if valor > 5]

maiores_que_cinco = [
    valor  # RESULTADO
    for valor in valores  # PARA CADA ELEMENTO NA SEQUENCIA
    if valor > 5  # SE CONDIÇÃO
]

print(valores)
print(maiores_que_cinco)
