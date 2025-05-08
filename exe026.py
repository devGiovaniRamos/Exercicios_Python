#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = input('Digite uma frase: ').lower().strip()
a = frase.count('a')
pa = frase.find('a')+1
ua = frase.rfind('a')+1
print('Existem {} "A" na frase'.format(a))
print('O primeiro "A" encontra-se na posição {}'.format(pa))
print ('O ultimo "A" encontra-se na posição {}'.format(ua))
