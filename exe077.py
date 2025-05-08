# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
from operator import index

lista = 'FAMILIA', 'DEUS', 'VIOLAO', 'CASA', 'CARRO', 'GIOVANI', 'GUITARRA', 'MERCADO'

for v in lista:
    print ((v),'possui as vogais:',end=' ')
    for vogal in v:
        if vogal in 'AEIOU':
            print(vogal.lower(),end=' ')
    print('\n')
