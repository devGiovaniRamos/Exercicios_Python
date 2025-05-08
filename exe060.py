# Faça um programa que leia um número qualquer e mostre o seu fatorial.
print('-=-'*4,'!FATORANDO!', '-=-'*4)
n1 = int(input('Digite o número que deseja fatorar: '))
cont = n1 * (n1 - 1)
print('{}! = {} x'.format(n1, n1), end=' ')
n1 -= 1
while n1 != 1:
    print('{} x'.format(n1), end=' ')
    n1 -= 1
    cont = cont * n1
    if n1 == 1:
        print('1 =', end=' ')
print(cont)

