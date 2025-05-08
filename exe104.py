#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaint(n):
    if n.isnumeric():
        return f'O valor {n} é numérico'
    else:
        return '\033[31mERRO! valor não numérico\033[31m'


n = leiaint(input('Digite um n: '))
print(n)