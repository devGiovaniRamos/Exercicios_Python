# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

entrada = soma = cont = maior = 0
menor = 99999999
parar = ''
while parar != 'S':
    entrada = int(input('Digite um número.'))
    soma += entrada
    cont += 1
    if entrada > maior:
        maior = entrada
        maior_contador = cont
    if entrada < menor:
        menor = entrada
        menor_contador = cont
    parar = input('Deseja parar ? [S/N] ').upper().strip()
print('Você digitou {} número(s) e a soma total foi {}'.format(cont, soma))
if cont > 1:
    print('A média entre todos os valores digitados é {:.1f}'.format(soma / cont))
    print('O {}° número,{}, foi o maior e o {}° número,{}, foi o menor'.format(maior_contador,maior,menor_contador,menor))