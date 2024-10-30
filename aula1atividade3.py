import math
print('vamos calcular equação de segundo grau que legal :(')
a = float(input('Escreva o primeiro numero '))
b = float(input('Escreva o segundo numero '))
c = float(input('Escreva o terceiro numero '))
d = float(input('escreva o quarto numero '))
x1 = ((-b) + (b**2-4*a*(c - d))**0.5)/(2*a)
x2 = ((-b) - (b**2-4*a*(c - d))**0.5)/(2*a)
print(f'x1={x1} e x2={x2}')