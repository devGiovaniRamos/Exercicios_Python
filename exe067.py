# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

cont = 1
while True:
    n = int(input('Qual número deseja calcular ?: '))
    if n < 0:
        print('PROGRAMA ENCERRADO')
        break
    for c in range (1,11):
        print(f'{n} x {cont} = {n * cont}')
        cont += 1
    cont = 1
    n = 0
