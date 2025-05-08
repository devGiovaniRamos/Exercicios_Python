# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se
# a expressão passada está com os parênteses abertos e fechados na ordem correta.

exp = input('Digite sua expressão: ')
a = []
for p, l in enumerate(exp):
    if l == '(':
        a.append(l)
    elif l == ')':
        if '(' in a:
            a.pop()
        else:
            a.append('(')
if a == list():
    print('Expressão correta!!!')
else:
    print('Expressão incorreta!!!')
