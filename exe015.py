d = int (input ('Quantos dias o carro ficou alugado ?: '))
km = float (input ('Quantos quilômetros percorreu ?: '))
s = (d*60)+(km*0.15)
print ('O total a pagar é de R${:.2f}'.format(s))