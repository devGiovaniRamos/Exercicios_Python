import math
x = float( input('Digite um ângulo em graus: '))
seno = math.sin((math.radians(x)))
coss = math.cos((math.radians(x)))
tan = math.tan((math.radians(x)))
print ('O ângulo de {} tem como seno {:.2f}, como cosseno {:.2f} e como tangente {:.2f}'.format(x, seno, coss, tan))
