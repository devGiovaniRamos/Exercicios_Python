# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista_alunos = []
aluno_nota = []
cont = 1
while True:
    aluno_nota.append(str(input(f'Nome aluno {cont}: ')))
    aluno_nota.append(float(input('Nota 1: ')))
    aluno_nota.append(float(input('Nota 2: ')))
    lista_alunos.append(aluno_nota[:])
    aluno_nota = []
    cont += 1
    sn = input('Deseja adicionar ? (S/N): ')
    if sn in 'Nn': break
print('-='*20)
for c, a in enumerate(lista_alunos):
    print(f'Aluno n°{c +1}: {a[0]:.<12} ',end='')
    med = (lista_alunos[c][1] + lista_alunos[c][2]) /2
    if med < 5: print(f'Média: \033[31m{med}\033[m')
    else: print(f'Média: \033[32m{med}\033[m')
print('-='*20)
while True:
    m = (input('Deseja mostrar notas do aluno ? (Digite n°/ "N" para parar): '))
    if m in 'Nn':
        print('Programa finalizado. Até mais!')
        break
    n = int(m) - 1
    if 0 <= n < len(lista_alunos):
        print(f'{lista_alunos[n][0]} Nota 1: {lista_alunos[n][1]} Nota 2: {lista_alunos[n][2]}')
    else:
        print('Número não adicionado')
