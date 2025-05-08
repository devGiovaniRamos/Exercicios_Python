#  Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
#  0 – 1 – 1 – 2 – 3 – 5 – 8
print('-_-_'* 3, 'SEQUÊNCIA DE FIBONACCI', '-_-_'* 3)
seq = int(input('Quantos termos voçê quer mostrar: '))
print('0' if seq == 1 else '0 -> 1', end='')
if seq == 1:
    cont = 1
else:
    cont = 2
t1 = 0
t2 = 1
t3 = 0
while cont != seq:
    cont += 1
    t3 = t1 + t2
    print(' -> {}'.format(int(t3)), end='')
    t1 = t2
    t2 = t3
