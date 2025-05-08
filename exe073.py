# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Vasco.

tabela = ('', 'Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corinthias', 'Bahia',
          'Cruzeiro', 'Vasco', 'Vitória', 'Atlético MG', 'Fluminense', 'Grêmio', 'Juventude', 'Bragantino',
          'Atlhetico PR', 'Criciúma', 'Atlético GO', 'Cuiabá')

print(f'Os 5 primeiros colocados do Brasileirão 24 foram {tabela[1:6]}')
print(f'Os últimos 4 colocados foram {tabela[17:21]}')
print(f'Em ordem alfabética fica {sorted(tabela)}')
print(f'O Vasco da Gama terminou em {tabela.index('Vasco')}°')