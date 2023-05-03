# desafio 17
# faça um programa que leia o cateto oposto e o cateto adjacente de um
# triângulo retângulo, calcule e mostre o comprimento da hipotenusa;

from math import hypot
c1 = float(input('Digite o valor do cateto oposto: '))
c2 = float(input('Digite o valor do cateto adjacente: '))
print('O valor da hipotenusa é {:.2f}.'.format(hypot(c1, c2)))
