# desafio 11
# faça um programa que leia a altura e a largura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m²;

alt = float(input('Digite a altura, em metros, da parede: '))
lar = float(input('Digite a largura, em metros, da parede: '))
tinta = (alt*lar)/2
print('Para pintar essa área de parede, serão necessários {} litros de tinta.'.format(tinta))
