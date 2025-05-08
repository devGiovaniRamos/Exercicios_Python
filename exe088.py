# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep

jogos = int(input('Quantos jogos deseja gerar ?: '))
bilhetes = list()
b = []
for c in range(jogos):
    for n in range(6):
        r = randint(1,60)
        while True:
            if r in b:
                r = randint(1, 60)
            else:
                break
        b.append(r)
    bilhetes.append(b[:])
    b.clear()
cont = 1
for e, n in enumerate(bilhetes):
    print(f'Bilhete {cont} {sorted(n)}')
    sleep(0.7)
    cont += 1

