from os import system
from time import sleep
from random import choice
print('Eu pensei em um número e DUVIDO você descobrir !!!')
print('REGRA: você terá 3 chances para descobrir o número de 1 a 10, OK ?')
lista = choice([1,2,3,4,5,6,7,8,9,10])
n = int(input('Digite um número: '))
if lista == n:
    print('DE PRIMEIRA ? PARABÉNS VOCÊ ACERTOU !!!')
    exit()
else:
    print('Você errou mas tente novamente')
n = int(input('Digite um número: '))
if lista == n:
    print('PARABÉNS VOCÊ ACERTOU !!!')
    exit()
else:
    print('Você errou, mas ainda tem uma chance')
n = int(input('Digite um número: '))
if lista == n:
    print('PARABÉNS VOCÊ ACERTOU NA SUA ÚLTIMA CHANCE !!!')
    exit()
else:
    print('Você errou, que pena ! O número que eu escolhi era {}'.format(lista))
    print('Seu computador será desligado em 10 segundos kkkkk')
    sleep(10)
    system('shutdown /s /t 1')
