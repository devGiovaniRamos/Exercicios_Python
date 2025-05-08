#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome “SANTO”.
c = input('Digite o nome de uma cidade: ')
ci = (c.split()[0]).upper()
print (ci == 'SANTO')
