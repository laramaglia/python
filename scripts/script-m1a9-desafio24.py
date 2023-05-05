# desafio 24
# crie um programa que leia o nome de uma cidade e diga se ela começa ou não
# com o nome SANTO;

cidade = input('Digite o nome da cidade: ')
cidade = cidade.upper()
cidade = cidade.strip()
print(cidade[:5] == ('SANTO'))







