# desafio 27
# Faça um programa que leia o nome completo de uma pessoa e, mostrando em
# seguida o primeiro e o último nome separadamente;
# ex: Ana Maria de Souza
# Primeiro = Ana
# Último = Souza

nome = input('Escreva seu nome completo: ').strip()
nome = nome.split()
print('Primeiro nome: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[len(nome)-1]))