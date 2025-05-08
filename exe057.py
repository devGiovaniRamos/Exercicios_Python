# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a
# digitação novamente até ter um valor correto.
sexo = input('Digite seu sexo (M/F):').upper()
while sexo not in 'MF':
    print('Seleção inválida, tente novamnete.\n'
          'OBS: M = masculino / F = feminino.')
    sexo = input('Digite seu sexo (M/F):').upper()
if sexo == 'M':
    print('Você selecionou o sexo MASCULINO')
if sexo == 'F':
    print('Você selecionou o sexo FEMININO')
