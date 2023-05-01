# desafio 007
# Desenvolva um programa que leia as duas notas de um aluno, calcule
# e mostre a sua média;
print('='*50)
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2
print('\nA média do aluno é de {:.1}.'.format(media))
print('='*50)