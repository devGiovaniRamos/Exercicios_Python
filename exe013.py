s = float( input( 'Digite aqui seu salário: R$'))
a = float( input ('Digite aqui a % (porcentagem) do seu aumento:  '))
res = (s/100)*a+s
print ('Parabéns !!! Seu salário é de R${:.2f}'.format(res))