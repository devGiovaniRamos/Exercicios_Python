# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista.
from operator import index

lista = []
maior = []
menor = []
for c in range(5):
    lista.append(int(input(f'Digite o {c+1}° número: ')))
print(lista)
print(f'O maior valor digitado foi: {max(lista)}, na: ', end='')
for v, l in enumerate(lista):
    if l == max(lista):
        print(f'{v+1}ª...',end='')
print(' posição(ões)')
print(f'\nO menor valor digitado foi: {min(lista)}, na: ',end='')
for vm, lm in enumerate(lista):
    if lm == min(lista):
        print(f'{vm+1}ª...',end='')
print(' posição(ões)')


