import math
print('Olá eu sou uma calculadora de renda fixa vamos multiplicar a sua grana?')
capital = float(input('quanto voçê vai aplicar? '))
taxa = float(input('qual é a taxa de juros anual? '))
tempo = float(input('Qual é o tempo de aplicacão? '))
montante = capital * (1 + (taxa/100))**tempo
juros = montante - capital
montante = capital + juros
print(f'O valor total do seu investimento à {tempo} anos atras te rendeu um total de R${math.ceil(montante)}')
