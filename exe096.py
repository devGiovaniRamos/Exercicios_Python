# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

def area(l,c):
    print(f'Esse terreno de {l} x {c} tem: {l*c}m².')


print('=== CALCULADORA DE M² ===')
print(area(float(input('Digite a largura (m): ')), float(input('Digite o comprimento (m): '))))
