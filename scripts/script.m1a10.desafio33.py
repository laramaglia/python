# desafio 33
# faça um programa que leia 3 números e mostre qual é o maior e qual é o menor;

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
n3 = int(input('Digite o último número: '))

# Verificando o maior valor:
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2

if n3 < n1 and n3 < n2:
    menor = n3

# Verificando o menor valor:
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2

if n3 > n1 and n3 > n2:
    maior = n3

print('O menor número é {}.'.format(menor))
print('O maior número é {}.'.format(maior))


#if n1 > n2 and n1 > n3:
#    print('O maior número é {}.'.format(n1))
#else:
#        if n1 < n2 and n1 < n3:
#            print('O menor número é {}.'.format(n1))
#
#if n2 > n1 and n2 > n3:
#    print('O maior número é {}.'.format(n2))
#else:
#        if n2 < n1 and n2 < n3:
#            print('O menor número é {}.'.format(n2))
#
#if n3 > n1 and n3 > n2:
#    print('O maior número é {}.'.format(n3))
#else:
#        if n3 < n1 and n3 < n2:
#            print('O menor número é {}.'.format(n3))



