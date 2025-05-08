#  Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade
#  do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
idade_total= 0
idade_ind = 0
homem_mais_v = ''
mulheres_sub = 0
pess = 0
for c in range (4):
    pess += 1
    print('___'*2, pess,'° pessoa','___'*2)
    nome = input('Qual o nome da {}° pessoa ?: '.format(pess))
    sexo = input('Digite seu sexo: ').upper().strip()
    idade = int(input('Digite sua idade: '))
    idade_total += idade
    if sexo == 'MASCULINO' and idade > idade_ind:
        homem_mais_v = nome
        idade_ind = idade
    if sexo == 'FEMININO' and idade < 20:
        mulheres_sub += 1
print('A média de idade do grupo é de {:.0f} anos'.format(idade_total/4))
print('O homem mais velho do grupo é o {}'.format(homem_mais_v))
print('{} mulher(es) tem menos de 20 anos'.format(mulheres_sub))




