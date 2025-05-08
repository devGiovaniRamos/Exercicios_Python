# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep


def maior(* n):
    cont = maior = 0
    for valor in n:
        print(f'{valor}')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
    print(f'O maior valor é {max(maior)}')

lista = []
c = 1
while True:
    num = int(input(f'Digite o {c}º número: '))
    lista.append(num)
    c += 1
    sn = input('Deseja continuar [S/N]: ')
    if sn in 'Nn':
        break
tupla = tuple(lista)
maior(tupla)