# desafio 014
# conversor de temperatura ºC e ºF;

c = float(input('Informe a temperatura em ºC: '))
f = c * 1.8 + 32 #ou (9*c/5)+32
print('A temperatura de {}ºC corresponde a {:.1f}ºF.'.format(c, f))