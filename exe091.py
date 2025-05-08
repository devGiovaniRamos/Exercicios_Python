# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado
from operator import itemgetter
from random import randint
from time import sleep

lista = {'jogador 1': randint(1,6), 'jogador 2': randint(1,6),
         'jogador 3': randint(1,6), 'jogador 4': randint(1,6)}

for k, v in lista.items():
    print(f'{k} jogou o dado: {v}')
    sleep(1)
print('-='*20)
print('=== RANKING ===')
lista_ordem = sorted(lista.items(), key=itemgetter(1), reverse=True)
for c, l in enumerate(lista_ordem):
    print(f'{c+1}ºlugar: {l[0]} com {l[1]} ')

