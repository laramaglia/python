# desafio 31
# desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens até 200km
# e R$0,45 para vigens mais longas;

dis = float(input('Digite a distância em km da viagem: '))
# val = dis * 0.50 if dia <= 200 else dis * 0.45
if dis <= 200:
    val = float(0.50 * dis)
    print('O valor da passagem é de R${:.2f}.'.format(val))
else:
    val = float(0.45 * dis)
    print('O valor da passagem é de R${:.2f}.'.format(val))