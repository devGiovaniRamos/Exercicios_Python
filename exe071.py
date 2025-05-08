# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
# a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('-=-'*4, '\033[4;34mBEM VINDO AO BANCO GRM\033[m', '-=-'*4,'\n')
print('\033[33mOBS: O caixa possui cédulas de R$50, R$20, R$10 e R$1.\033[m')
saque = int(input('Quanto deseja sacar ? R$'))
cont_cinq = cinquenta = cont_vin = vinte = cont_dez = dez = cont_um = um = 0
while cinquenta < saque:
    cinquenta += 50
    cont_cinq += 1
    if cinquenta > saque:
        cinquenta = (cinquenta - 50)
        cont_cinq = (cont_cinq - 1)
        break
vinte = cinquenta
while vinte < saque:
    vinte += 20
    cont_vin += 1
    if vinte > saque:
        vinte = (vinte - 20)
        cont_vin = (cont_vin - 1)
        break
dez = vinte
while dez < saque:
    dez += 10
    cont_dez += 1
    if dez > saque:
        dez = (dez - 10)
        cont_dez = (cont_dez - 1)
        break
um = dez
while um < saque:
    um += 1
    cont_um += 1
    if um > saque:
        um = (um - 1)
        cont_um = (cont_um - 1)
        break
if cont_cinq > 0: print(f'Total de {cont_cinq} cédulas de R$ 50,00')
if cont_vin > 0: print(f'Total de {cont_vin} cédulas de R$ 20,00')
if cont_dez > 0: print(f'Total de {cont_dez} cédulas de R$ 10,00')
if cont_um > 0: print(f'Total de {cont_um} cédulas de R$ 1,00')