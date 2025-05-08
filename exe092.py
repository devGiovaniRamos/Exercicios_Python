# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar

import datetime

infos = {}
infos['nome'] = input('Digite seu nome completo: ')
infos['Ano de nascimento'] = int(input('Ano de nascimento: '))
infos['CTPS'] = int(input('Número CTPS: '))
if infos['CTPS'] != 0:
    infos['Ano de contratação'] = int(input('Ano de contratação: '))
    infos['Salário'] = int(input('Salário: '))

idade_n = infos['Ano de nascimento']
ano = datetime.date.today().year
idade = ano - idade_n
print(f'Seu nome é {infos['nome']}\n Idade atual: {idade} anos')
if infos['CTPS'] != 0:
    aposent = infos['Ano de contratação'] + 30 - idade_n
    print(f'Carteira de Trabalho: {infos['CTPS']}\n Idade que se aposentará: {aposent}')

