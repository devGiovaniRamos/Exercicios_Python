# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
# todos os valores pares sorteados pela função anterior.
from random import randint

lista = []


def sorteia(a):
    for c in range(5):
        num = randint(1,10)
        a.append(num)
    print(f'A lista sorteada foi: {a}')


def somapar(a):
    soma = 0
    for c in a:
        if c % 2 == 0:
            soma += c
    print(f'Os valores pares somado dessa lista é: {soma}')


sorteia(lista)
somapar(lista)




