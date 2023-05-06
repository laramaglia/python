# desafio 34
# Escreva um programa que aumento o salário de um funcionário e calcule o valor
# do seu aumento;
# Para salários superiores a R$1250,00, calcule um aumento de 10%;
# Para salários infriores ou iguais, o aumento é de 15%;

sal = float(input('Digite seu salário: '))

if sal > 1250:
    salau = sal + (sal / 100 * 10)
else:
    salau = sal + (sal / 100 * 15)

print('Seu salário foi reajustado de R${:.2f} para R${:.2f}.'.format(sal, salau))