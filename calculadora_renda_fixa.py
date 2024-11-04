import math
print('Olá eu sou uma calculadora de renda fixa vamos multiplicar a sua grana?')
c = float(input('quanto voçê vai aplicar? '))
i = float(input('qual é a taxa de juros anual? '))
n = float(input('Qual é o tempo de aplicacão? '))
m = c * (1 + (i/100))**n
j = m - c
m = c + j
print(f'O valor total do seu investimento à {n} anos atras te rendeu um total de R${math.ceil(m)}')