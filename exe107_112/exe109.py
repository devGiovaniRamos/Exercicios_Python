# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor
# retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moeda

valor = moeda.dobrar(int(input('Digite valor: ')))
sn = input('Deseja formatar como moeda ? [S/N] ')
if sn in 'Ss':
    valor = moeda.moeda(valor)
print(valor)