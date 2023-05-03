# desafio 16
# crie um programa que leia um numero real qualquer pelo teclado e mostre na
# tela a sua porção inteira;
# ex: digite um número: 6.127
# o número 6.127 tem a parte inteira 6

from math import trunc
num = float(input('Digite um número qualquer: '))
print('A parte inteira de {} é {}.'.format(num, trunc(num)))

# dessa forma se atinge o mesmo objetivo:
'''num = float(input('Digite um número qualquer: '))
print('A parte inteira de {} é {}.'.format(num, int(num)))'''
