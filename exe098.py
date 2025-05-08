#  Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
#  Seu programa tem que realizar três contagens através da função criada:
#  a) de 1 até 10, de 1 em 1
#  b) de 10 até 0, de 2 em 2
#  c) uma contagem personalizada

from time import sleep

def contador(a,b,c):
    print('-='*20)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if a < b:
        cont = a
        while cont <= b:
            sleep(0.5)
            print(f'{cont}', end=' ')
            cont += c
        print()
    else:
        cont = a
        while cont >= b:
            sleep(0.5)
            print(f'{cont}', end=' ')
            cont -= c
        print()


contador(1,10,1)
contador(10, 0, 2)
print('AGORA SUA VEZ')
contador(a= int(input('Início: ')), b=int(input('Fim: ')), c=int(input('Passo: ')))