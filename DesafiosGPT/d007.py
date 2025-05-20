def cont_palavras(texto):
    import re
    texto = re.sub(r'[^\w\s]', '', texto)
    texto = texto.lower().split()
    dicionario = {}
    for p in texto:
        if p in dicionario:
            dicionario[p] += 1
        else:
            dicionario[p] = 1
    print (dicionario)


cont_palavras(texto=input('Digite algo: '))
