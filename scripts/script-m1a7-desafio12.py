# desafio 012
# faça um algoritmo que leia o preço de um produto e mostre o seu novo preço,
# com 5% de desconto;

pre = float(input('Digite o valor do produto: R$'))
des = pre - (pre/100)*5 #ou (pre * 5 /100)
print('O valor do produto, com desconto de 5% aplicado, é de R${:.2f}.'.format(des))