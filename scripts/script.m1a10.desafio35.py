# desafio 35
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
# se elas podem ou não formar um triângulo;

r1 = int(input('Indique o comprimento da primeira reta: '))
r2 = int(input('Indique o comprimento da segunda reta: '))
r3 = int(input('Indique o comprimento da terceira reta: '))

if r3 < r1 + r2 and r2 < r1 + r3 and r1 < r2 + r1:
    print('As retas podem formar um triângulo.')
else:
    print('As retas não podem formar um triângulo.')
