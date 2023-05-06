n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média é {:.1f}.'.format(m))
if m >= 6.0:
    print('Parabéns, a sua média está boa!')
else:
    print('Sua média não está boa, estude mais!')

# condição simplificada:
# print('Parabéns! if m >= 6.5 else 'Estude mais!')


