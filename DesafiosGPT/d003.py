frase = str(input('Digite uma frase: ')).replace(' ', '').lower()
frase_invertida = (frase[::-1])
if frase == frase_invertida:
    print(f'A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')
print(f'{frase}\n{frase_invertida}')
