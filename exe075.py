# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares
from operator import index

v0 = int(input('Digite o 1° valor: '))
v1 = int(input('Digite o 2° valor: '))
v2 = int(input('Digite o 3° valor: '))
v3 = int(input('Digite o 4° valor: '))
valores = v0, v1, v2, v3
print(valores)
print('O número nove apareceu ', valores.count(9), 'vezes')
if 3 in valores:
    print('O primeiro número 3 foi digitado na posição', valores.index(3) + 1)
else: print('O número 3 não foi digitado')
print('São números pares: ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')





