# desafio 45
# Game: Pedra, Papel, Tesoura

# cores
cores = {'amarelo':'\033[1;33m',
         'verde':'\033[1;32m',
         'vermelho':'\033[1;31m',
         'azul':'\033[1;34m',
         'limpa':'\033[m'}

# jogada do computador
from random import randint

jokenpo = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)

# jogada do usuário
user = int(input('''Escolha um:
            [0] - PEDRA;
            [1] - PAPEL;
            [2] - TESOURA;
            ---> '''))

# duelo
print('Você {}{}{} {}X{} {}{}{} Computador'.format(cores['amarelo'], jokenpo[user], cores['limpa'], cores['azul'], cores['limpa'], cores['amarelo'], jokenpo[pc], cores['limpa']))
if user == pc:
    print('{}{:-^30}'.format(cores['amarelo'], 'EMPATE!'))
elif user == 2 and pc == 1 or user == 0 and pc == 2 or user == 1 and pc == 0:
    print('{}{:-^30}'.format(cores['verde'], 'VOCÊ GANHOU!'))
else:
    print('{}{:-^30}'.format(cores['vermelho'], 'VOCÊ PERDEU!'))

# {:-^30} significa que nos espaço de 30 caracteres,
# a string ficará centralizada e o espaço vazio será preenchido por '-';
