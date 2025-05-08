# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

lista = ('lápis', 1.50,
         'borracha',1.00,
         'caderno', 25.99,
         'apontador', 0.50,
         'estojo', 6.99,
         'mochila',  99.99,
         'caneta', 2.00,
         'lapizera', 2.50,
         'grafite',5.99,
         'lápis de cor', 12.90)
for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f'{lista[i]:.<30}', end='')
    else:
        print(f'R$ {lista[i]:>5.2f}')
