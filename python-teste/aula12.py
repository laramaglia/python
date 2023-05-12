cores = {'limpa':'\033[m',
         'nome':'\033[4;36m',
         'frase':'\033[1;34m'
}

nome = input('Qual é o seu nome? ')

if nome == 'Lara':
    print('{}Que nome bonito!{}'.format(cores['frase'], cores['limpa']))
elif nome == 'Silvia' or nome == 'Claudia':
    print('{}Que nome diferente!{}'.format(cores['frase'], cores['limpa']))
elif nome in 'Pedro Paulo Leonardo João':
    print('{}O que tenho a ver...{}'.format(cores['frase'], cores['limpa']))
else:
    print('{}Seu nome é bem normal.{}'.format(cores['frase'], cores['limpa']))

print('Tenha um bom dia, {}{}{}!'.format(cores['nome'],nome, cores['limpa']))
