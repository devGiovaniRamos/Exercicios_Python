#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
# Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
km = float(input('Digite a distancia da viagem em km: '))
km1 = km * 2.7
km2 = km * 3.6
if km <= 20:
    print('O valor de sua viagem é de R${:.2f}'.format(km1))
    exit()
print('O valor de sua viagem é de R${:.2f}'.format(km2))