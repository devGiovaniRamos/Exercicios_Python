def agrupar_digitos(args):
    args = args.split()
    num = list()
    for n in args:
        num.append(int(n))
    dicionario = {}
    for n in num:
        num_unid = abs(n) % 10
        if num_unid in dicionario:
            dicionario[num_unid].append(n)
        else:
            dicionario[num_unid] = [n]
    print(dicionario)


agrupar_digitos((input('Digite: ')))
        