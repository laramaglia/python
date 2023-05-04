# desafio 20
# o mesmo professor do desafio 19 quer sortear a ordem de apresentação dos alunos.
# faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada;

import random
a1 = input('Nome do alune: ')
a2 = input('Nome do alune: ')
a3 = input('Nome do alune: ')
a4 = input('Nome do alune: ')
list = [a1, a2, a3, a4]
random.shuffle(list)
print('A ordem de apresentação será a seguinte:\n{}'.format(list))
