# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

pt = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 0
for c in range (1, 11):
    cont = cont + 1
    print ('O {}° termo é: {}'.format(cont, pt))
    pt = pt + razao