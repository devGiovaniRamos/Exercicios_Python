# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista = list()
l = list()
while True:
    l.append(input('Digite seu nome: '))
    l.append(int(input('Digite seu peso: ')))
    lista.append(l[:])
    l = list()
    sn = input('Deseja adicionar mais alguém ? (S/N): ')
    if sn in 'Nn':
        break
print(f'Foram cadastradas: {len(lista)} pessoas.')
print('O(a) mais pesado(a):', end=' ')
peso = []
for c, p in enumerate(lista):
    peso.append(p[1])
print(f'{lista[peso.index(max(peso))][0]} com {max(peso)}KG\n')
print(f'O(a) mais leve: {lista[peso.index(min(peso))][0]} com {min(peso)}KG')

