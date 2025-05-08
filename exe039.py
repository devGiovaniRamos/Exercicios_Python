from datetime import date
data = date.today().year
nome = input('Digite seu nome completo: ').split()
print('Olá, {}!'.format(nome [0]))
nas = int(input('{}, digite o ano que nasceu: '.format(nome [0])))
ida = int(data - nas)
if ida == 18:
    print('{}, você deve se alistar na junta militar mais próxima até 30 de junho.'.format(nome [0]))
elif ida > 18:
    pas = ida - 18
    print('Você deveria ter se alistado há {} atrás.'.format(pas))
else:
    fal = 18 - ida
    print('{}, falta {} anos para você completar a idade de alistamento obrigatório. '.format(nome [0],fal))
