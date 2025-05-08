# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
# números gerados e também indique o menor e o maior valor que estão na tupla.

from random import sample

lista = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
emb = sample(lista, 5)
print(emb)
print(f'O maior número é {max(emb)} e o menor é {min(emb)}')


