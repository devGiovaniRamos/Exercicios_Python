#  Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
#  separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
numim = []
numpar = []
for c in range(7):
    n = (int(input('Digite um número: ')))
    if n % 2 == 0:
        numpar.append(n)
    else:
        numim.append(n)
listanum = [numpar] + [numim]
print(f'Valores pares: {sorted(listanum[0])}')
print(f'Valores ímpares: {sorted(listanum[1])}')
