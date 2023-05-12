# desafio 41
# A confederação nacional de natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:
# até 9 anos: MIRIM
# até 14 anos: INFANTIL
# até 19 anos: JUNIOR
# até 20 anos: SÊNIOR
# acima MASTER

from datetime import date

anoatual = date.today().year
anonasc = int(input('Digite o ano de nascimento da pessoa atleta: '))
idade = anoatual - anonasc

if idade <= 9:
    print('ATLETA MIRIM')
elif idade > 9 and idade <= 14:
    print('ATLETA INFANTIL')
elif idade > 14 and idade <= 19:
    print('ATLETA JUNIOR')
elif idade == 20:
    print('ATLETA SÊNIOR')
else:
    print('ATLETA MASTER')
