# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#  A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.
cont_idade = cont_homens = cont_mulheres = cont_pessoas = 0
while True:
    nome = input('Qual seu nome:')
    sexo = input('Digite seu sexo M/F:').strip().upper()
    if sexo == 'M':
        cont_homens += 1
    idade = int(input('Digite sua idade:'))
    if idade >= 18:
        cont_idade += 1
    if sexo == 'F' and idade < 20:
        cont_mulheres += 1
    cont_pessoas += 1
    print('Cadastro finalizado.')
    loop = input('CADASTRAR NOVO USUÁRIO ? (S)sim (N)não.').upper().strip()
    if loop != 'S':
        break
print(f'Foram cadastrados {cont_pessoas} pessoas, {cont_homens} são homem(ns), {cont_idade} pessoas são maiores de 18, '
      f'{cont_mulheres} são mulheres menores de 20 anos. ')