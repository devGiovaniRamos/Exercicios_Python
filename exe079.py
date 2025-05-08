# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
cont = 1
while True:
    valor = int(input(f'Digite o {cont}° valor para adicionar a lista: '))
    if valor not in lista:
        lista.append(valor)
    cont += 1
    parar = input('Deseja continuar adicionando ? (S/N): ').upper().strip()
    if parar == 'N':
        break
print(sorted(lista))