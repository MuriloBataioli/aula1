import math
print('Olá sou uma calculadora de notas escolares \n vamos calcular algumas notas?')
n1 = float(input('A nota da primeira prova '))
n2 = float(input('A nota da segunda prova '))
print('Ok vamos ver qual é o peso de cada uma das provas(a nota minima necessaria para passar)')
p1 = float(input('O peso da primeira prova '))
p2 = float(input('O peso da segunda prova '))
p3 = float(input('O peso a ultima prova '))
Mf = (p1 + p2 + p3) - (n1 + n2)
print(f'A nota necessaria para passar é {Mf}')
if Mf > 10:
    print('vai passar não kkkkkkk')
elif Mf <= 10:
    print('tu ainda consegue passar tente')