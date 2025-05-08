# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
from time import sleep


def ajuda(a):
    """
    -> Escanea biblioteca do pycharm para achar a descrição da função desejada
    :param a: nome da função para pesquisa
    :return: retorna a descrição da função pedida
    """
    print('LOADING',end='')
    sleep(0.3)
    print('.',end='')
    sleep(0.3)
    print('.',end='')
    sleep(0.3)
    print('.',end='')
    sleep(0.3)
    print('')
    print('\033[44m~' * 30)
    print(f'{a:^30}')
    print('~'* 30)
    print('\033[1;7;40m')
    m = 'Manual comando'
    return (f'{m},{help(a)}')


while True:
    print('\033[m''\033[42m~' * 30)
    print('\033[42m   INTERACTIVE HELP PYTHON     ')
    print('\033[42m~' * 30)
    aj = input('\033[mQual função deseja ver ? ["s" para sair]: ')
    if aj in 'Ss':
        print('FINALIZANDO.',end='')
        sleep(0.7)
        print('.',end='')
        sleep(0.7)
        print('.',end='')
        sleep(0.7)
        print('\n\033[42mATÉ MAIS')
        break
    else:
        ajuda(aj)
