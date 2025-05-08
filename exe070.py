# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total_compras = cont_mil = pre_prod_barato = nom_prod_barato = 0
while True:
    produto = input('Digite o nome do produto: ')
    preco = int(input('Digite seu valor: '))
    total_compras += preco
    if preco > 1000:
        cont_mil += 1
    if pre_prod_barato == 0:
        pre_prod_barato = preco
        nom_prod_barato = produto
    else:
        if preco < pre_prod_barato:
            nom_prod_barato = produto
            pre_prod_barato = preco
    parar = input('Deseja incluir mais um produto ? (S/N) ').strip().upper()
    if parar == 'N':
        break
print(f'O total de gasto em compras foi de {total_compras}R$ \n {cont_mil} produtos custam mais de 1000R$'
      f' \n {nom_prod_barato} é o produto mais barato custando {pre_prod_barato}R$')
