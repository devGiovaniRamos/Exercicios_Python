# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno_nota = {}
aluno_nota['Nome'] = input('Nome: ')
aluno_nota['Média'] = float(input('Média: '))
if aluno_nota['Média'] >= 6:
    aluno_nota['Situação'] = 'Aprovado'
elif 3.9 < aluno_nota['Média'] and aluno_nota['Média'] < 6:
    aluno_nota['Situação'] = 'Recuperação'
else:
    aluno_nota['Situação'] = 'Reprovado'
print('-='*20)
for n, m in aluno_nota.items():
    print(f'{n} do aluno: {m}')
