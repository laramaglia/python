# desafio 22
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1- O nome com todas a letras maiúsculas;
# 2- O nome com todas as letras minúsculas;
# 3- Quantas letras ao (todo sem considerar espaços);
# 4- Quantas letras tem o primeiro nome;

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em letras maiúsculas fica {}.'.format(nome.upper()))
print('Seu nome em letras minúsculas fica {}.'.format(nome.lower()))
print('A quantidade de letras no seu nome é de {}.'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('O seu primeiro nome é {} e tem {} letras.'.format(separa[0], len(separa[0])))
#print('O seu primeiro nome tem {} letras.'.format(nome.find(' ')))



