#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior  O segundo valor é maior Não existe valor maior, os dois são iguais
x = int (input('Digite um número: '))
y =  int (input('Digite o segundo número: '))
lis = x, y
if y == x:
    print('Não existe valor maior, os dois são iguais.')
elif max(lis) == x:
    print('O primeiro valor é maior.')
elif max(lis) == y:
    print('O segundo valor é maior.')