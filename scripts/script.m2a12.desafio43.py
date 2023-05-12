# desafio 43
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre
# seu status de acordo com a tabela abaixo:
# Abaixo de 18.5: abaixo do peso;
# Entre 18.5 e 25: peso ideal;
# de 25 até 30: Sobrepeso;
# 30 até 40: obesidade;
# Acima de 40: obesidade mórbida;

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('IMC de {:.1f}, ABAIXO DO PESO.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('IMC de {:.1f}, PESO IDEAL.'.format(imc))
elif imc >= 25 and imc < 30:
    print('IMC de {:.1f}, SOBREPESO.'.format(imc))
elif imc >= 30 and imc < 40:
    print('IMC de {:.1f}, OBESIDADE.'.format(imc))
else:
    print('IMC de {:.1f}, OBESIDADE MÓRBIDA.'.format(imc))