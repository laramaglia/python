# desafio 23
# faça um programa que leia de 0 a 9999 e mostre na tela cada um dos dígitos
# separados. ex: digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

num = int(input('Digite um número entre 0 a 9999: '))
print(num)
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
