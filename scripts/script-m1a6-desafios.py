# desafio 003
# crie um programa que leia dois números e mostre a soma entre eles;

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = (n1+n2)
print('A soma entre {} e {} é {}'.format(n1, n2, soma))

# desafio 004
# crie um programa que leia algo pelo teclado e mostre na tela o seu tipo
# primitivo e todas as informações sobre ele;

val = input('Digite algo: ')
print(type(val))
print('Posso imprimir {}?'.format(val))
print(val.isprintable())
print('{} é alfa-numérico?'.format(val))
print(val.isalnum())
print('{} é composto por letras?'.format(val))
print(val.isalpha())
print('{} contém apenas caracteres ASCII (American Standard Code for Information Interchange)?'.format(val))
print(val.isascii())
print('{} é composto de dígitos?'.format(val))
print(val.isdigit())
print('{} é um identificador?'.format(val))
print(val.isidentifier())
print('{} é um decimal?'.format(val))
print(val.isdecimal())
print('{} é em minúsculas?'.format(val))
print(val.islower())
print('{} é em maiúsculas?'.format(val))
print(val.isupper())
print('{} é numérico?'.format(val))
print(val.isnumeric())
print('{} é um título?'.format(val))
print(val.istitle())
print('{} é um espaço?'.format(val))
print(val.isspace())
