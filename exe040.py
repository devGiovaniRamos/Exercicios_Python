# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
# média atingida:
n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite sua nota: '))
med = (n1 + n2) / 2
if med < 5:
    print('Sua média é {}, você foi REPROVADO.'.format(med))
elif 5 < med < 6.9:
    print('Sua média é {}, você está de RECUPERAÇÃO.'.format(med))
elif med >= 7:
    print('Parabéns ! Sua média é {}, você foi APROVADO.'.format(med))