#  Crie um programa que faça o computador jogar Jokenpô com você.
import random
from time import sleep
x = 'PEDRA PAPEL TESOURA'.split()
print('_' * 27)
print ('__________\033[1;;41mJOKENPÔ\033[m__________')
nome = input('Olá !?:')
print('Olá {}, borá uma partida de jokenpô ?'.format(nome)),sleep(2)
print('As opções você já sabe: PEDRA, PAPEL ou TESOURA !!!'),sleep(2.3)
print('Eu escolho...hmm... JÁ SEI!!!'),sleep(1)
cpu = random.choice(x)
print('Bora lá, eu já escolhi !!! ')
ppt = input('Agora escolha você: ').upper()
if ppt != 'PEDRA':
    if ppt != 'PAPEL':
        if ppt != 'TESOURA':
            print('Não existe essa opção BURRO!')
            exit()
print('\033[31mPEDRA\033[m'),sleep(0.6)
print('PAPEL'),sleep(0.6)
print('\033[35mTESOUUURA!!!\033[m')
print ('{} x {}'.format(cpu, ppt)),sleep(1)
if cpu == 'PEDRA' and ppt == 'TESOURA':
    print('HAHAHA GANHEI !!!')
elif cpu == 'PAPEL' and ppt == 'PEDRA':
    print('OPA papel vence pedra GANHEI !!!')
elif cpu == 'TESOURA' and ppt == 'PAPEL':
    print('CORTEI, quer dizer, GANHEI !!!')
elif cpu == ppt:
    print('EMPATOU :)')
else:
    print('PERDI :(')
