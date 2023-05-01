# desafio 005
# Faça um programa que leia um número inteiro e mostre na tela o seus sucessor
# e o seu antecessor;

print('='*60)
n = int(input('| Digite um número: '))
print('| O número sucessor de {} é {} e o seu antecessor é {}.'.format(n, (n+1), (n-1)))
print('='*60)
print()

# desafio 006
# crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo
# e a raiz quadrada;

print('='*60)
n1 = int(input('| Digite um número: '))
print('| O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.3}.'.format(n1, n1*2, n1*3, n1**(1/2)))
print('='*60)
print()