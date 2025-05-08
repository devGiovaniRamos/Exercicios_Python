#  Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas
#  partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em
#  um dicionário, incluindo o total de gols feitos durante o campeonato.

infos = {}
infos['Nome'] = input('Nome do jogador: ')
infos['Partidas'] = int(input('Número de partidas jogadas: '))
totgols = 0
for c in range(infos['Partidas']):
     nump = f'p{c+1}'
     infos[nump] = int(input(f'Gols na {c+1}º partida: '))     #Até aqui funcionando legal
     totgols += infos[nump]
print('-='*30)
print(f'{infos} {totgols}')
print('-='*30)
print(f'{infos['Nome']}, você tem um total de {totgols} gols em {infos['Partidas']} partidas.\n'
      f' aproveitamento de {totgols / infos['Partidas']:.2f} gols por partida.')
print('-='*30)
print(f'O jogador {infos["Nome"]} jogou {infos["Partidas"]} partidas.')
for c in range(infos['Partidas']):
    nump = f'p{c+1}'
    print(f'Partida {c+1} fez {infos[nump]} gols')
