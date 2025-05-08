#  Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um
#  valor monetário formatado.

import moeda

valor = moeda.aumentar(float(input('Digite valor: ')))
valor = moeda.moeda(valor)
print(valor)