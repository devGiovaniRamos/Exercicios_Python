#  Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
from time import sleep
soma = 0
contador = 0
for n in range (1,501,2):
    if n % 3 == 0:
        contador = contador + 1
        soma = soma + n
print('A soma entre os {} números é de {}'.format(contador, soma))