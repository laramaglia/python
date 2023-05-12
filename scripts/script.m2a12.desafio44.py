# desafio 44
# Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço
# normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto;
# - à vista no cartão: 5% de desconto;
# - em até duas vezes no cartão: preço normal;
# - 3x no cartão ou mais: 20% de juros;

valor_prod = float(input('Digite o valor do produto: R$'))
forma_pag = int(input('''Escolha a forma de pagamento:
                  [1] - À vista no dinheiro ou cheque;
                  [2] - À vista no cartão;
                  [3] - 2x no cartão;
                  [4] - 3x ou mais no cartão;
                  ---> '''))
# a string entre três aspas simples é uma string literal que pode conter várias
# linhas sem a necessidade de utilizar a quebra de linha como separador;

if forma_pag == 1:
    valor_prod = valor_prod - (valor_prod * 10 / 100)
    print('O valor final do produto, com 10% de desconto, fica R${:.2f}.'.format(valor_prod))
elif forma_pag == 2:
    valor_prod = valor_prod - (valor_prod * 5 / 100)
    print('O valor final do produto, com 5% de desconto, fica R${:.2f}.'.format(valor_prod))
elif forma_pag == 3:
    print('O valor total a pagar é de R${:.2f} em duas percelas de R${:.2f}.'.format(valor_prod, valor_prod / 2))
elif forma_pag == 4:
    parcelas = int(input('Número de parcelas: '))
    valor_prod = valor_prod + (valor_prod * 20 / 100)
    print('O valor final do produto, com 20% de juros, fica R${:.2f} dividido em {} vezes de R${:.2f}.'.format(valor_prod, parcelas, valor_prod / parcelas))
else:
    print('Opção inválida.')
