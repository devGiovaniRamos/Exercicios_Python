#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores.
from datetime import datetime
jovem = 0
velho = 0
pessoa = 0
ano_atual = int(datetime.now().year)
for c in range (1,8):
    pessoa = pessoa + 1
    idade = int(input('Qual a idade da {}° pessoa: '.format(pessoa)))
    if ano_atual - idade >= 18:
        velho += 1
    else:
        jovem += 1
print('Ao todo tivemos {} pessoas maiores de idade\ne também {} pessoas menores de idade.'.format(velho,jovem))



