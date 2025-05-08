#  Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
#frase = input('Digite a frase: ').upper()
#frase_sem_espaco = frase.replace(' ', '')
#frase_invertida = frase_sem_espaco[::-1]
#if frase_sem_espaco == frase_invertida:
 #   print('A frase {} É um palíndromo {} .'.format(frase_sem_espaco, frase_invertida))
#else:
 #   print('A frase {} NÃO é palíndromo {}'.format(frase_sem_espaco, frase_invertida))

frase =  str(input('Digite uma frase: ')).upper().strip()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range (len(junto)-1,-1,-1):
    inverso += (junto[letra])
if inverso == junto:
    print('A frase {} É um palíndromo {} .'.format(junto, inverso))
else:
    print('A frase {} NÃO é palíndromo {}'.format(junto, inverso))


