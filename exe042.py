# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais ISÓSCELES: dois lados iguais, um diferente ESCALENO: todos os lados diferentes
a = float (input('Digite a reta A: '))
b = float (input('Digite a reta B: '))
c = float (input('Digite a reta C:'))
if a < b + c and b < a + c and c < a + b:
    print('\033[1;32mSim ! é possível formar um triangulo.')
    if a == b == c:
        print('CLASSIFICAÇÃO: EQUILÁTERO: (todos os lados iguais).')
    if a == b != c or a == c != b or b == c != a:
        print('CLASSIFICAÇÃO: ISÓSCELES: (dois lados iguais).')
    if a != b and a != c:
        print('CLASSIFICAÇÃO: ESCALENO: (todos os lados diferentes).')
else:
    print('\033[1;31mNão é possivel formar um triangulo.')
