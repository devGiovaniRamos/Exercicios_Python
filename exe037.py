#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
#conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
print('           Conversor de números.')
print('-=-'*15)
numero = int(input('Digite um número: '))
print('(A) binário\n(B) hexadecimal\n(C) octal')
x = input('Digite a letra correspondente a base que deseja converter: ').upper()
if x == 'A':
    bi = bin(numero)
    print('O número {} será {}, convertido para bínario.'.format(numero,bi[2:]))
elif x == 'B':
    he = hex(numero)
    print('O número {} será {}, convertido para hexadecimal.'.format(numero,he[2:]))
elif x == 'C':
    oc = oct(numero)
    print('O número {} será {}, convertido para octal.'.format(numero,oc[2:]))

