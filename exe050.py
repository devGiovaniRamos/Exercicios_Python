#  Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#  Se o valor digitado for ímpar, desconsidere-o.

soma = 0
for n in range (1,6):
    n = int (input('Digite um número: '))
    if n % 2 == 0:
        soma = soma + n
print('Somando apenas os números pares o resultado é {}'.format(soma))