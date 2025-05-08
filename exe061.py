# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print('-=-'*3,'GERADOR DE PA', '-=-'*3)
t1 = int(input('1° termo: '))
razao = int(input('Razão da PA: '))
rep = 1
cont = 0
acum = t1
nt = int(input('n° de termos: '))
while rep == 1:
    while cont != nt:
        cont += 1
        print('{}'.format(acum), end='')
        print(' >>> ' if cont != nt else '', end='')
        acum += razao
    print('\nDESEJA CONTINUAR ?\n[ 1 ] SIM\n[ 2 ] NÃO')
    rep = int(input('...'))
    if rep == 2:
        print('PA finalizada com {} termos.'.format(cont))
        exit()
    nt1 = int(input('n° de termos a mais: '))
    if nt1 == 0:
        print('PA finalizada com {} termos.'.format(cont))
        exit()
    nt += nt1






