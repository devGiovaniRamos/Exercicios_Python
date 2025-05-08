# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano):
    from datetime import date
    a = date.today().year
    condicao = a - ano
    print(f'Idade atual: {condicao} anos',end=' | ')
    if 16 <= condicao < 18 or condicao > 65:
        return 'VOTO OPCIONAL'
    elif 18 <= condicao < 65:
        return 'VOTO OBRIGATÓRIO'
    else:
        return 'VOTO NEGADO'


nas=(int(input('Digite seu ano de nascimento: ')))
print(voto(nas))