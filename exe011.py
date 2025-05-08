print ('Calcule a quantidade de tinta para pintar sua parede')
lar = float (input ('Largura: '))
alt = float (input ('Altura: '))
res = (lar*alt)/2
print ('Sua parede mede', lar*alt,'m², e você gastará {:.2} litros de tinta.'.format (res))
print ('ATENÇÃO: A conta foi baseada no gasto de 1 litro de tinta para 2m²')