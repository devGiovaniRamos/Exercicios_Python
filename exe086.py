# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[],[],[],[],[],[],[],[],[]]
letra = 'A'
cont = 1
for c in range(0,9):
    if c == 3:
        letra = 'B'
    if c == 6:
        letra = 'C'
    valor = int(input(f'Coluna {letra}{cont}: '))
    if cont == 3:
        cont = 1
    else:
        cont += 1
    for l in range(9):
        matriz[c].append(valor)
        break
cont = 0
for m in enumerate(matriz):
    if cont == 3 or cont == 6:
        print('')
    print(f'{matriz[cont]}',end='')
    cont += 1
