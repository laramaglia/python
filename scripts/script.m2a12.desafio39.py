# Desafio 39
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua
# idade:
# Se ele ainda vai se alistar no serviço militar;
# Se é a hora de se alistar;
# Se já passou do tempo de alistamento;
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo;

from datetime import datetime

ano = int(input('Digite o seu ano de nascimento: '))
anoatual = datetime.now().year
idade = anoatual - ano
print(idade)

if idade < 18:
    print('Você deverá se alistar no serviço militar em {} anos.'.format(18 - idade))
elif idade == 18:
    print('Você está com {} anos, é hora de se alistar.'.format(idade))
else:
    print('Você atrasou em {} anos o seu alistamento no serviço militar.'.format(idade - 18))
