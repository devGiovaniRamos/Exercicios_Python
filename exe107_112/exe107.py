# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

valor = moeda.aumentar(int(input('Digite o valor a ser acrescído 10%: ')))
print(valor)

valor = moeda.diminuir(int(input('Digite o valor a ser subtraído 10%: ')))
print(valor)

valor = moeda.dobrar(int(input('Digite o valor a ser multiplicado: ')))
print(valor)

valor = moeda.dividir(int(input('Digite o valor a ser dividido: ')))
print(valor)
