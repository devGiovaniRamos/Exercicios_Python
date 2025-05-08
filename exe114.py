# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib.request
import urllib.error

try:
    urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print('Site não acessível')
else:
    print('Site funcionando')