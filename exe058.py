# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint

lista = randint (0, 10)
print('Pensei em um número, tente acerta-lo. DICA: entre 0 e 10')
jogador = int(input('Qual número pensei ?: '))
tentativas = 1
while jogador != lista:
    tentativas += 1
    if jogador > lista:
        print('Você errou, tente novamente\n DICA: o número é menor que {} '.format(jogador))
    if jogador < lista:
        print('Você errou, tente novamente\n DICA: o número é maior que {} '.format(jogador))
    jogador = int(input('Digite novamente: '))
print('Parabéns, foi exatamente o número {} que pensei.\n Você acertou na {}° tentativa'.format(lista, tentativas))


