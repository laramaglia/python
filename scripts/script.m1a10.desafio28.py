# desafio 28
# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
# pelo computador;
# O programa deverá escrever na tela se o usuário venceu ou perdeu;

from random import randint
n = randint(0, 5)
nu = int(input('Tente adivinhar o número de 0 a 5: '))
if nu == n:
    print('Você acertou! O número sorteado é {}!'.format(nu))
else:
    print('Você errou, o número sorteado foi {}.'.format(n))