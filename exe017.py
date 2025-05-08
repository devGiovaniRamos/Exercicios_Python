import math
co = float( input('Digite o comprimento do cateto oposto: '))
ca = float( input('Digite o comprimrnto do cateto adjacente: '))
hip = math.hypot(co, ca)
print ('A hipotenusa é {:.2f}'.format(hip))
