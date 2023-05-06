# desafio 29
# Escreva um programa que leia a velocidade de um carro;
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado;
# A multa vai custa R$ 7,00 por cada km excedido;

vel = float(input('Digite a velocidade do carro em km: '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Você recebeu uma multa no valor de R${:.2f} por excesso de velocidade.'.format(multa))
else:
    print('Você está dentro do limite de velocidade.')
print('Tenha um bom dia! DIRIJA COM SEGURANÇA!')