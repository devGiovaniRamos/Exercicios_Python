# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
# aproveitamento de cada jogador.

jog = []
infos = {}
totgols = 0
while True:
    infos['Nome'] = input('Nome do jogador: ')
    infos['Partidas'] = int(input('Número de partidas jogadas: '))
    for c in range(infos['Partidas']):
        nump = f'p{c+1}'
        infos[nump] = int(input(f'Gols na {c+1}º partida: '))
        totgols += infos[nump]
    infos['Total de gols'] = totgols
    jog.append(infos.copy())
    infos.clear()
    sn = input('Deseja adicionar outro jogador ? [S/N] ')
    if sn in 'Nn':
        break
print('-='*40)
for x in jog:
    print(f'{x}')
print('-='*30)
for x in jog:
    media = x['Total de gols'] / x['Partidas']
    print(f'Atleta {x["Nome"]} | {x["Total de gols"]} gols | {x["Partidas"]} partidas.')
    print(f'Aproveitamento de {media:.1f} por partida')
    print('-='*20)
for x in jog:
    print(f'O jogador {x["Nome"]} jogou {x["Partidas"]} partidas.')
    for c in range(x['Partidas']):
        nump = f'p{c+1}'
        print(f'Partida {c+1} fez {x[nump]} gols')
    print('-='*20)