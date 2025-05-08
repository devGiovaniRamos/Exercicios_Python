# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
t1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 0
acum = t1
while cont != 10:
    cont += 1
    print('O {}° termo é: {}'.format(cont, acum))
    acum += razao
