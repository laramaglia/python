# desafio 25
# Crie um programa que leia o nome de uma pessoa e diga se ela tem silva no nome;

nome = input('Digite seu nome completo: ').strip()
nome = nome.lower()
print('Seu nome tem Silva? {}.'.format('silva' in nome))


#nome = nome.find('silva')
#if nome == -1:
#    print('Não contém o sobrenome Silva.')
#else:
#    print('Contém o sobrenome Silva')
