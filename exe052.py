# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n1 = int(input('Digite um número: '))
x = 0
for c in range (1, n1 + 1):
    if n1 % c == 0:
        x =  x + 1
        print('\033[32m{}'.format(c),end=' ')
    else:
        print('\033[31m{}'.format(c),end=' ')
if x == 2:
    print('\n\033[mO número {} foi divisível 2 vezes, por isso ele \033[32mÉ PRIMO\033[m.'.format(n1))
else:
    if n1 == 1:
        print('\n\033[mO número {} foi divisível {} vez, por isso ele \033[31mNÃO É PRIMO\033[m.'.format(n1, x))
    else:
        print('\n\033[mO número {} foi divisível {} vezes, por isso ele \033[31mNÃO É PRIMO\033[m.'.format(n1,x))
print('\033[33mENTENDA:\033[m um número é primo quando ele for divisível 2 vezes com resto zero sendo apenas por 1 e por ele mesmo.')

