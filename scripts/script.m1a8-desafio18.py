# desafio 18
# faça um programa que leia um ângulo qualquer e mostre na tela o valor
# do seno, cosseno e tangente deste valor;

from math import cos, tan, sin, radians
ang = float(input('Digite o valor de um ângulo qualquer: '))
angr = radians(ang)
print('O seno do ângulo {} é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}.'.format(ang, sin(angr), cos(angr), tan(angr)))
