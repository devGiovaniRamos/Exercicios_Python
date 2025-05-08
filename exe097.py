# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre
# uma mensagem com tamanho adaptável.

def escreva(a):
    t = len(a) + 4
    print('~'* t)
    print(f'  {a}')
    print('~' * t)


while True:
    a = input('Digite um título: ')
    escreva(a)
    sn = input('Escrever outro título ? [S/N]:')
    if sn in 'Nn':
        break