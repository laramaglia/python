# desafio 10
# crie um programa que mostre quando dinheiro uma pessoa tem na carteira
# e quantos dólares ela pode comprar;

val = float(input('Digite o valor disponível em R$: '))
dolar = val/4.99
euro = val/5.49
parg = val*0.023
iene = val*0.037
print('R${:.2f} convertido para dólares fica US${:.2f}.'.format(val, dolar))
print('R${:.2f} convertido para euros fica EU${:.2f}.'.format(val, euro))
print('R${:.2f} convertido para pesos argentinos fica AR${:.2f}.'.format(val, parg))
print('R${:.2f} convertido para ienes fica JPY{:.2f}.'.format(val, iene))
