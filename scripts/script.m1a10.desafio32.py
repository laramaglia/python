# desafio 32
# faça um programa que leia um ano e mostre se ele é bissexto;

from datetime import date
#se o valor digitado for 0, este módulo importa o ano atual da máquina;

ano = int(input('Digite o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # != significa diferente de;
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))

