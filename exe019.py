from random import choice
n1 = input('Digite o nome 1: ')
n2 = input('Digite o nome 2: ')
n3 = input('Digite o nome 3: ')
n4 = input('Digite o nome 4: ')
lista = [n1,n2,n3,n4]
r = choice(lista)
print ('O nome escolhido foi {} !!!'.format(r))
