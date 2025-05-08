# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
cont = 0
tab = 0
n = int (input('Digite um número: '))
for x in range (1, 11):
    tab = tab + 1
    cont = n * x
    print('{} x {} = {}'.format(n, tab, cont))
