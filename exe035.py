# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
a = float (input('Digite a reta A: '))
b = float (input('Digite a reta B: '))
c = float (input('Digite a reta C:'))
if a < b + c and b < a + c and c < a + b:
    print('\033[1;32mSim ! é possível formar um triangulo.')
else:
    print('\033[1;31mNão é possivel formar um triangulo.')