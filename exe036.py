carro = float(input('Digite o valor do veículo: R$'))
renda = int(input('Qual a sua renda: R$'))
anos = float(input('Em quantos anos pretende pagar: '))
meses = anos * 12
carxme = carro / meses
if carxme >= (renda * 0.30):
    print('Seu empréstimo foi negado.')
else:
    print('Parabéns !!! Seu empréstimo foi aprovado no valor de {:.0f}x de R${:.2f}.'.format(meses, carxme))