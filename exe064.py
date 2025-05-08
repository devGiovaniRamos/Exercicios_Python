#  Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
#  valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
entrada = 0
soma = 0
cont = 0
while entrada != 999:
    entrada = int(input('Digite um número [999 pra parar]'))
    if entrada != 999:
        soma += entrada
        cont += 1
print('Você digitou {} número(s) e a soma total foi {}'.format(cont, soma))
