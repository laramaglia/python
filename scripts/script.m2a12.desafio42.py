# desafio 42
# Refaça o desafio 35 dos triângulos:
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
# se elas podem ou não formar um triângulo;
# Mas agora acrescente o recurso de mostrar qual triângulo foi formado:
# - Equilátero: todos os lados iguais;
# - Isóceles: dois lados iguais;
# - Escaleno: todos os lados diferentes;

r1 = int(input('Indique o comprimento da primeira reta: '))
r2 = int(input('Indique o comprimento da segunda reta: '))
r3 = int(input('Indique o comprimento da terceira reta: '))

if r3 < r1 + r2 and r2 < r1 + r3 and r1 < r2 + r1:
    print('As retas podem formar um triângulo.')
    if r1 == r2 and r1 == r3:
        print('Este triângulo é equilátero.')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Este triângulo é isóceles.')
    else:
        print('Este triângulo é escaleno.')
else:
    print('As retas não podem formar um triângulo.')

