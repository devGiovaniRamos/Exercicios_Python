from idlelib.replace import replace


def aumentar(a):
    """
    função para aumentar 10% o valor adicionado
    :param a: valor adicionado
    :return: valor acrescido de 10 %
    """
    moed = a * 1.10
    return f'{moed:.0f}'


def diminuir(a):
    """
    função para diminuir 10% o valor de a
    :param a: valor adicionado
    :return: valor - 10%
    """
    moed = a * 0.90
    return f'{moed:.0f}'


def dobrar(a):
    """
    função para dobrar o valor de a
    :param a: valor adicionado
    :return: valor x 2
    """
    moed = a * 2
    return f'{moed:.0f}'


def dividir(a):
    """
    função para dividir o valor de 'a' ao meio
    :param a: valor adicionado
    :return: valor / 2
    """
    moed = a / 2
    return f'{moed:.0f}'



def moeda(a):
    """
    função para formatar valor em ordem monetária
    :param a: valor adicionado
    :return: valor em ordem monetária
    """
    moed = int(a)
    return f'R${moed:.2f}'.replace('.',',')