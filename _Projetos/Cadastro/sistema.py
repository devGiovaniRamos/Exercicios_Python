
from time import sleep
from lib.interface import *
from lib.arquivo import *

arquivo='Banco de dados.txt'
if not arqExiste(arquivo):
    criarArq(arquivo)

while True:
    menu(['Ver usuários cadastrados', 'Cadastrar novo usuário', 'Sair do programa'])
    try:
        o=int(input('Selecione uma opção: '))
        if o == 1:
            cabecalho('USUÁRIOS CADASTRADOS')
            lerArq(arquivo)
        elif o == 2:
            cabecalho('CADASTRO DE NOVO USUÁRIO')
            cadastrar(arquivo, nome=input('Nome: '), idade=int(input('Idade: ')))
        elif o == 3:
            cabecalho('PROGRAMA FINALIZADO')
            break
        else:
            print(color('v'),'Opção inválida, tente novamente',color(''))
            continue
    except (ValueError, TypeError):
        print(color('v'),'ERRO! selecione com os caracteres [1], [2] ou [3]',color(''))
        continue





