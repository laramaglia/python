# desafio 26
# Faça um programa que leia a frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'A';
# Em que posição ela aparece a primeira vez;
# Em que posição ela aparece a última vez;

frase = input('Digite uma frase: ').strip()
frase = frase.lower()
print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira letra A se encontra na posição {}.'. format(frase.find('a')+1))
print('A letra A aparece pela última vez na posição {}.'.format(frase.rfind('a')+1))


