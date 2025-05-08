#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
pessoa = 0
ma = 0
mi = 999
pessoama = 0
pessoami = 0
for c in range (1,6):
    pessoa += 1
    peso = float(input('Digite o peso da {}° pessoa: '.format(pessoa)))
    if peso > ma:
        pessoama = pessoa
        ma = peso
    elif peso < mi:
        pessoami = pessoa
        mi = peso
print('O maior e o menor peso da lista são, respectivamente, da {}° pessoa com {}KG e'
      ' da {}° pessoa com {}KG.'.format(pessoama, ma, pessoami, mi))


