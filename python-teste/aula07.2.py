n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1+n2
d = n1/n2
m = n1*n2
di = n1//n2
e = n1**n2
# {:.3f} significa que depois do ponto tem 3 casas de números flutuantes;
# para dois prints separados serem exibidos na mesma linha, use end=
# \n quebra a linha no meio da string;
print('A soma vale {}, a divisão \n é de {:.3f}, o produto é de {},'.format(s, d, m), end=' ')
print('a divisão inteira \n é de {} e a potência é de {}.'.format(di, e))