#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 100 == 0:
    print('O ano de {} É BISSEXTO!!!.'.format(ano))
else:
    print('O ano de {} NÃO É bissexto.'.format(ano))
