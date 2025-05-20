num = int(input('Digite um número: '))
n = num
vistos = set()
print(f'{num}', end=' | ')
while True:
    n = sum(int(digito) ** 2 for digito in str(n))

    print(f'{n}', end=' | ')

    if n == 1:
        print(f'O número {num} É FELIZ!!!')
        break
    elif n in vistos:
        print(f'O número {num} não é feliz :(')
        break
    else:
        vistos.add(n)