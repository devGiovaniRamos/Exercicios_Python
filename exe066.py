# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

n = 0
cont = 0
acum = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    else:
        cont += 1
        acum += n
print(f'Foram digitados {cont} número(s), a soma de todos é {acum}')


