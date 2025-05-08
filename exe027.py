#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = input('Digite seu nome: ')
print('Olá sr(a) {} {}'.format(nome.split()[0],nome.split()[-1]))
