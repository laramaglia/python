# desafio15
# calcule o valor a pagar pelo carro alugado, sabendo que a diária é de R$60 e
# R$0,15 o km rodado
dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos kilômetros foram rodados? '))
val = (dias * 60) + (km * 0.15)
print('O valor a pagar pelo aluguel é de R${:.2f}.'.format(val))
