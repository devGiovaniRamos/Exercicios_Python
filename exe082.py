# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = list()
lista_par = list()
lista_im = list()
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    if valor % 2 == 0:
        lista_par.append(valor)
    else:
        lista_im.append(valor)
    sn = input('Deseja continuar ? (S/N): ')
    if sn in 'Nn':
        break
print(f'Você digitou os valores: {lista}')
print(f'Os números pares são: {lista_par}')
print(f'Os números ímpares são: {lista_im}')
