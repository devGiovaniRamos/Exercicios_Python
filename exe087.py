# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[],[],[]]
cont = acum = lador = terf  = 0
mai2 = []
abc = 'ABC'
for c in range(1,10):
    if c == 4 or c == 7: cont += 1
    lador = int(input(f'Digite o valor {abc[cont]}{c}: '))
    if lador % 2 == 0: acum += lador
    matriz[cont].append(lador)
    if c == 3 or c == 6 or c == 9: terf += lador
    if c == 4 or c == 5 or c == 6: mai2.append(lador)
for m in range(3):
    print(matriz[m])
print(f'A soma de todos os números pares: {acum}')
print(f'A soma da terceira coluna: {terf}')
print(f'O maior valor da segunda linha: {max(mai2)}')
