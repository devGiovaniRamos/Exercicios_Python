# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador
# e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(a='', b= 0):
    if a == '':
        a = '<desconhecido>'
    return (f'O jogador {a} fez {b} gols no campeonato.')


a = input('Nome do jogador: ')
b = input('Gols marcados: ')
if b.isnumeric():
    b = int(b)
else:
    b = 0
print(ficha(a=a, b=b))
