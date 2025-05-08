#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular
#e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(numero, show=True):
    """
    :param numero: Valor a ser calculado o fatorial
    :param show: valor boleano. True = mostra o calculo, False = não mostra o calculo
    :return:
    """
    while True:
        if numero < 0:
            return 'NÃO É POSSIVEL CALCULAR FATORIAL DE NÚMEROS NEGATIVOS.'
        else:
            break
    if numero == 0:
        return '1'
    else:
        fatorial = 1
        for c in range(1, numero + 1):
            if show == True:
                print(f'{c}',end=' ')
                if c == numero:
                    print(':',end=' ')
                else:
                    print('x',end=' ')
            fatorial *= c
        return fatorial


print(fatorial(numero=int(input('Calcular fatorial de: '))))

