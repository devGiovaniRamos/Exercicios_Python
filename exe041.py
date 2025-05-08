# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade: Até 9 anos: MIRIM, Até 14 anos: INFANTIL, Até 19 anos: JÚNIOR,Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER
from datetime import date
data = date.today().year
ida = int(input('Digite o ano em que o atleta nasceu: '))
idade = int (data - ida)
if idade <= 9:
    print('O atleta possui {} anos'.format(idade))
    print('Sua categoria é MIRIM.')
elif idade > 9 and idade <= 14:
    print('O atleta possui {} anos'.format(idade))
    print('Sua categoria é INFANTIL.')
elif idade > 14 and idade <= 19:
    print('O atleta possui {} anos'.format(idade))
    print('Sua categoria é JÚNIOR.')
elif idade > 19 and idade <= 25:
    print('O atleta possui {} anos'.format(idade))
    print('Sua categoria é SÊNIOR.')
elif idade > 25:
    print('O atleta possui {} anos'.format(idade))
    print('Sua categoria é MASTER.')
