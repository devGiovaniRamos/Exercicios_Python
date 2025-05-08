# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta
# de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = list()
cont = 1
for c in range(5):
    valor = int(input(f'Digite o {cont}° valor: '))
    cont += 1
    if not lista:
        lista.append(valor)
        print('Adicionado no final da lista')
    else:
        for p, v in enumerate(lista):
            if valor <= v:
                lista.insert(p, valor)
                print(f'Adicionado na posição {p+1}')
                break
        if valor > v:
            lista.append(valor)
            print('Adicionado no final da lista')
print(lista)