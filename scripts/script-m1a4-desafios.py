print('1º Desafio Python: crie um Script Python que leia o nome de uma pessoa ')
print('e escreva uma mensagem de boas vindas de acordo com o valor digitado.')
print('-----------------------------------------------------------------------')
print()

nome = input('Olá, qual é o seu nome? ')
print()
print('Prazer em te conhecer, ', nome,'!')
print('=======================================================================')
print()

print('2º Desafio Python: crie um Script Python que leia o dia, o mês e o ano ')
print('de nascimento de uma pessoa e mostre uma mensagem com a data formatada.')
print('-----------------------------------------------------------------------')
print()

dia = input('Digite o dia do seu nascimento: ')
mês = input ('Digite o mês do seu nascimento: ')
ano = input ('Digite o ano do seu nascimento: ')
print()
print('Data de nascimento de ', nome,':', dia, '/', mês, '/', ano)
print('=======================================================================')
print()

print('2º Desafio Python: crie um Script Python que leia dois números tente ')
print('mostrar a soma entres eles.')
print('-----------------------------------------------------------------------')
print()

n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')
soma = int(n1) + int(n2)
print()
print('O valor da soma entre ',n1, 'e', n2,'é de ', soma)
#neste execício precisei inserir a função int para que os número fossem somados
#e não juntados pq input lê este valor como string e não números.
#esta observação serve apenas para esta aula com o conteúdo até aqui aprendido.









