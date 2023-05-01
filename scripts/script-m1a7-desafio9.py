# desafio 009
# faça um programa que leia um número inteiro qualquer
# e mostre na tela a sua tabuada;

n = int(input('Digite um número: '))
print('='*60)
print('TABUADA DE {}'.format(n))
print('  1X{} = {:.<7}  2X{} = {:.<7} 3X{} = {:.<7}  4X{} = {:.<7}'.format(n, n*1, n, n*2, n, n*3, n, n*4))
print('  5X{} = {:.<7}  6X{} = {:.<7} 7X{} = {:.<7}  8X{} = {:.<7}'.format(n, n*5, n, n*6, n, n*7, n, n*8))
print('  9X{} = {:.<7} 10X{} = {:.<6} 11X{} = {:.<7} 12X{} = {:.<7}'.format(n, n*9, n, n*10, n, n*11, n, n*12))
print('='*60)