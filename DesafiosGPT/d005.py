frase1 = str(input('Frase 1: '))
frase2 = str(input('Frase 2: '))

fraseset1 = set(frase1.replace('.', '').replace(',', '').lower().split())
fraseset2 = set(frase2.replace('.', '').replace(',', '').lower().split())

palavras_ambas = fraseset1 & fraseset2
palavras_unicas1 = fraseset1 - fraseset2
palavras_unicas2 = fraseset2 - fraseset1
cont_palavras = len(fraseset1 ^ fraseset2)

print(f'Palavras únicas da frase 1: {palavras_unicas1}')
print(f'Palavras únicas da frase 2: {palavras_unicas2}')
print(f'Palavras que apareceram em ambas as frases: {palavras_ambas}')
print(f'Palavras diferentes entre as duas frases: {cont_palavras}')
