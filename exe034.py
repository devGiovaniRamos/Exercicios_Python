#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores
# a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite seu salário: '))
if salario > 1250:
    ns = float (salario / 100 * 10  + salario)
    print('\033[4;32mSeu novo salário será R${:.2f}'.format(ns))
else:
    ns = float (salario / 100 * 15 + salario)
    print('\033[4;32mSeu novo salário será R${:.2f}'.format(ns))