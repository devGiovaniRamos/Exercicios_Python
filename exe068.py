# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando
# o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
print('ÍMPAR OU PAR')
vit = 0
while True:
    op = int(input('Você escolhe ÍMPAR (1) ou PAR (2) ?: '))
    j = int(input('Digite um número de 1 a 10: '))
    cpu = randint(1,10)
    resultado = (j + cpu) % 2
    if resultado == 0:
        if op == 1:
            print(f'Eu escolhi {cpu}, e você escolheu {j}, portanto eu GANHEI !')
            break
        else:
            print(f'Eu escolhi {cpu} e você escolheu {j}, portanto VOCÊ GANHOU, PARABÉNS !')
            vit += 1
    if resultado != 0:
        if op == 2:
            print(f'Eu escolhi {cpu}, e você escolheu {j}, portanto eu GANHEI !')
            break
        else:
            print(f'Eu escolhi {cpu} e você escolheu {j}, portanto VOCÊ GANHOU, PARABÉNS !')
            vit += 1
print(f'Você acumulou um total de {vit} vitórias. ')






