#  Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre
# seu status, de acordo com a tabela abaixo: IMC abaixo de 18,5: Abaixo do Peso Entre 18,5 e 25: Peso Ideal 25 até 30: Sobrepeso
# 30 até 40: Obesidade Acima de 40: Obesidade Mórbida
peso = float (input('Peso (KG):'))
altura = float (input ('Altura (ex:1.65):'))
imc = peso / (altura * altura)
if imc < 18.5:
    print ('Seu IMC é {:.1f} e você está abaixo do peso ideal.'.format(imc))
    exit()
elif imc < 25:
     print('Seu IMC é {:.1f} e você está no peso ideal.'.format(imc))
     exit()
elif imc < 30:
    print('Seu IMC é {:.1f} e você está com sobrepeso.'.format(imc))
    exit()
elif imc < 40:
    print('Seu peso é {:.1f} e você está com obesidade.'.format(imc))
    exit()
elif imc > 40:
    print('Seu IMC é {:.1f} e você está com obesidade mórbida.'.format(imc))
