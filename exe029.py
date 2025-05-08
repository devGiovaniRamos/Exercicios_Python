from time import sleep
print('             Calculadora de multas de transito')
print('-=-' *20)
print('OBS: a velocidade máxima permitida da via em questão é 80 km.')
print('-=-' *20)
km = int(input('Digite a velocidade da infração: '))
if km <= 80:
    print('Não há multa')
else:
    multa = (km - 80) *7
    print('O total a pagar é de R${}'.format(multa))
