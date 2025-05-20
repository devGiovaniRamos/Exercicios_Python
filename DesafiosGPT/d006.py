#Crie uma função que recebe uma string e verifica se ela é um palíndromo, desconsiderando espaços, acentos e letras maiúsculas/minúsculas.

def palindr(string):
    import unicodedata
    string = string.replace(' ', '').lower()
    string = unicodedata.normalize('NFD', string)
    string = ''.join(c for c in string if unicodedata.category(c) != 'Mn')
    string_invertida = string[::-1]
    if string == string_invertida:
        print('Essa frase é um palíndromo')
    else:
        print('Não foi identificado um palíndromo nessa frase')


palindr(string=input('Digite uma frase: '))
