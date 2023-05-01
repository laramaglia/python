# desafio 008
# Escreva um programa que leia um valor em metros e o exiba convertido em
# centímetros e milímetros;

m = float(input('Digite um valor em metros: '))
km = m/1000
hc = m/100
dam = m/10
dm = m*10
c = m*100
mm = m*1000
print('{} metros corresponde a {} decímetros, {} centímetros e {} milímetros.'.format(m, dm, c, mm))
print('e {} metros corresponde a {} quilômetros e {} hectômetros, e {} decâmetros.'.format(m, km, hc, dam))