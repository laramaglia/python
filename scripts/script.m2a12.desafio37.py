# desafio 37
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão;
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

num = int(input('Digite um número: '))
base = int(input('Escolha a base de conversão:\n 1 - binária; \n 2 - octal; \n 3 - hexadecimal;\n ----> '))

if base == 1:
    print('O número {} convertido para binário fica {}.'.format(num, bin(num)[2:])) # [2:] é o fatiamento, para os dois primeiros caracteres da conversão não aparecerem pois são desnecessários para o programa;
elif base == 2:
    print('O número {} convertido para octal fica {}.'.format(num, oct(num)[2:]))
elif base == 3:
    print('O número {} convertido para hexadecimal fica {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida.')