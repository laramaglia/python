# desafio 013
# faça um algoritmo que leia o salário de um funcionário e mostre seu novo
# salário, com 15% de aumento;

sal = float(input('Digite o valor do salário atual: R$'))
au = sal + (sal/100)*15

print('O valor do salário atualizado, com 15% de aumento, é de R${:.2f}.'.format(au))