preco = float(input('Qual valor do produto: R$'))
opcao = ['0', '1', '2', '3','4', '5', '6']
print('                    OPÇÕES DE PAGAMENTO')
print('-=-'*20)
print(' (0) 0x (dinheiro) \n (1) 1x \n (2) 2x \n (3) 3x \n (4) 4x \n (5) 5x \n (6) 6x')
tp =  int(input('Digite a opção de pagamento: '))
if tp > 6:
    print('Opcão inválida de pagamento. Tente novamente.')
    exit()
if tp == 0:
    print('O valor de pagamento total é R${:.2f} com 10% de DESCONTO!!!'.format(preco * 0.90))
elif tp == 1:
    print('O valor do pagamento total é R${:.2f} com 5% de DESCONTO!'.format(preco * 0.95))
elif tp == 2:
    print('O valor do pagamento total é R${:.2f} sem juros. As parcelas '
          'serão R${:.2f} em {}.'.format(preco, preco / 2, '2x'))
else:
    print('O valor do pagamento total é R${:.2f} com acréscimo de 20%.'
          ' As parcelas serão R${:.2f} em {}.'.format(preco * 1.20,preco * 1.20 / tp, str(tp) + 'x'))