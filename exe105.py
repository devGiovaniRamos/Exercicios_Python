# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)


def notas(* n, sit= False):
    """
    função criada para gerar dados de notas escolares em um dicionário. Mostra quantidade de notas, a maior e a menor
    nota recebida, uma média de todas as notas e caso ligado retorna também a condição ruim, regular ou boa.

    :param n: recebe valores (sem limite) para formar o dicionário
    :param sit: função sit escreve na tela a condição mediante a média, se menor que 5 ruim, ate 7 regular, até 10 boa
    :return: retorna toda o dicionário preenchido
    """
    resp = {}
    cont = 0
    acum = 0
    if sit == False:
        for c in n:
            cont += 1
            acum += c
        resp = {'total de notas': cont, 'maior':max(n), 'menor':min(n), 'média':acum/cont}
        return resp
    else:
        for c in n:
            cont += 1
            acum += c
        med = acum/cont
        if med < 5:
            sit = 'RUIM'
        elif 5 <= med <= 7:
            sit = 'REGULAR'
        else:
            sit = 'BOA'
        resp = {'total de notas': cont, 'maior':max(n), 'menor':min(n), 'média':acum/cont ,'situação':sit}
        return resp


resp = notas(4,9,6.7,5,2.5, sit=True)
print(resp)