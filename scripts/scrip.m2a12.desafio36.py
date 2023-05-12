# desafio 36
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O
# programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele
# vai pagar.
# Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário,
# se não o empréstimo será negado;

from time import sleep
cores = {'limpa':'\033[m',
       'verde':'\033[1;32m',
       'vermelho':'\033[1;31m',
       'azul':'\033[1;36m',
       'sub':'\033[4m'
}

# cabeçalho
print('{}='.format(cores['azul'])* 44)
print('          Caixa Econômica Federal'.upper())
print('-' * 44)
print('    Financiamento Minha Casa Minha Vida')
print('='* 44)
print(cores['limpa']) #limpa as cores do programa

# perguntas
print('{}Para ter seu empréstimo aprovado, responda as seguintes perguntas{}:'.format(cores['sub'], cores['limpa']))
print()
valtot = float(input('Valor total do imóvel a ser comprado: R$'))
sal = float(input('Valor do salário da pessoa a financiar?: R$'))
ano = int(input('Em quantos anos se pretende quitar o imóvel? '))
print()
print()
print('Aguarde a análise do seu empréstimo...')
print()
sleep(4)

# cálculos
porsal = sal/100 * 30
pres = valtot / (ano * 12)

# resultado
print('{}De acordo com seus dados, o valor do financiamento seria de {} vezes de R${:.3f}.{}'.format(cores['azul'], ano * 12, pres, cores['limpa']))

# condições
if pres <= porsal:
    print('{}Parabéns, seu empéstimo foi concedido!{}'.format(cores['verde'], cores['limpa']))
else:
    print('{}Infelizmente o empréstimo não pode ser concedido como desejado pelo valor '
          'da parcela exceder a porcentagem salarial permitida de 30%'.format(cores['vermelho']))


