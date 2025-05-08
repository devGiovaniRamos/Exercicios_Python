# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
from operator import index

lista = list()
cont = 0
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    cont += 1
    al = input('Deseja adicionar mais um valor ? (S/N): ').strip().upper()
    if al in 'Nn':
        break
print('-='*25)
print(f'A lista que você formou: {lista}\n'
      f'A lista em ordem decrescente: {sorted(lista, reverse=True)}\n')
if 5 in lista:
    print(f'O valor 5 foi digitado na posição {lista.index(5)+1}')

