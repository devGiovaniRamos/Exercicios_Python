#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('\033[7;40mDigite um número:\033[m '))
n2 = int(input('\033[7;40mDigite outro número:\033[m '))
n3 = int(input('\033[7;40mDigite mais um número:\033[m '))
lista = [n1,n2,n3]
ma = max(lista)
mi = min(lista)
print('\033[1;46mO maior número que você digitou foi\033[m {}{}{}'.format('\033[1;32m',ma,'\033[m'))
print('-=-'*13)
print('\033[1;46mO menor número que você digitou foi\033[m {}{}{}'.format('\033[1;31m',mi,'\033[m'))

