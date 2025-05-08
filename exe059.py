# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar  [ 2 ] multiplicar [ 3 ] maior[ 4 ] novos números [ 5 ] sair do programa  Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep

print('-=-'*2, 'CALCULADORA', '-=-'*2)
v1 = int(input('1° valor: '))
v2 = int(input('2° valor: '))
op = ''
while op != '5':
    print(' [1] SOMAR\n [2] MULTIPLICAR\n [3] MAIOR\n [4] NOVOS NÚMEROS\n [5] SAIR DO PROGRAMA    ')
    op = input('Qual sua opção ?: ')
    if op == '1':
        print('{} + {} é: >>> {}'.format(v1, v2, v1+v2))
        sleep(3)
    elif op == '2':
        print('{} x {} é: >>> {}'.format(v1, v2, v1*v2))
        sleep(3)
    elif op == '3':
        if v1 == v2:
            print('Não existe maior entre {} e {}'.format(v1, v2))
        else:
            print('Entre {} e {} o maior é: >>> {}'.format(v1, v2, max(v1,v2)))
        sleep(3)
    elif op == '4':
        v1 = int(input('1° valor: '))
        v2 = int(input('2° valor: '))
    elif op == '5':
        print('Finalizando programa.')
        sleep(1.2)
    else:
        print('-=-' * 10)
        print('Opção inválida, tente novamente.')
        print('-=-' * 10)
print('Até mais!!!')
sleep(0.5)


