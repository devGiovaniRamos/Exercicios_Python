# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de
# tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaint(a):
    while True:
        try:
            n=int(input(a))
        except (ValueError, TypeError):
            print('ERRO! digite um número válido...')
            continue
        else:
            return n


def leiafloat(b):
    while True:
        try:
            n=float(input(b))
        except ( ValueError, TypeError):
            print('ERRO! digite um número válido...')
            continue
        else:
            return n


numint=leiaint('Digite um número inteiro: ')
numflo=leiafloat('Digite um número com vírgula: ')
print(f'O número inteiro digitado foi {numint} e o número real foi {numflo}')