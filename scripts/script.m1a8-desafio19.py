# desafio 19
# um professor quer sortear um dos seus quatro alunos para pagar o quadro
# faça um programa que ajude lendo o nome deles e escrevendo o nome escolhido;

from random import choice
a1 = input('Alune 1: ')
a2 = input('Alune 2: ')
a3 = input('Alune 3: ')
a4 = input('Alune 4: ')
ran = [a1, a2, a3, a4]
print('{} é quem vai apagar o quadro!'.format(choice(ran)))

# função choice() de random;
