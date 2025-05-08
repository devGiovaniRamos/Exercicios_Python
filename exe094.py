# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade
# C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

lista = []
pessoa = {}
while True:
    pessoa['nome'] = input('Nome: ')
    pessoa['idade'] = int(input('Idade: '))
    pessoa['sexo'] = input('Sexo [M/F]: ')
    lista.append(pessoa.copy())
    pessoa.clear()
    sn = input('Deseja adicionar mais uma pessoa ? [S/N]: ')             # estrutura para obter dados do usuário
    if sn in 'Nn':
        break
print('-='*30)
print(f'Foram cadastrados {len(lista)} pessoas')                  # ler quantas pessoas foram cadastradas
print('-='*30)
idade = 0
for i in lista:
    idade += i['idade']                                         # soma todas as idades
print(f'A média de idade é de {idade/len(lista):.1f} anos')
print('-='*30)
print(f'Mulheres cadastradas:',end=' ')
for m in lista:
    if m['sexo'] in 'Ff':                                        # Apresenta só nome de mulheres cadastradas
        print(f'{m['nome']}',end='...')
print('\n','-='*30)
print('Pessoas com idade acima da média:',end=' ')
for v in lista:
    if v['idade'] > (idade/len(lista)):
        print(f'{v['nome']} com {v['idade']}', end=' ')            # Apresenta apenas pessoas com idade acima da média
print('\n','===PROGRAMA FINALIZADO===')
