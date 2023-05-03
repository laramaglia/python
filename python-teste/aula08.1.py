from math import sqrt, floor, ceil
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, floor(raiz)))

# math.floor arredonda o resultado da raiz para baixo;
# math.ceil arredonda o resultado da raiz para cima;
# se a biblioteca inteira for importada, deve-se especificar os cmando com math. antes
# exemplo: math.sqrt(num)
# mas se os comando importandos dorem especificados, seus nomes podem ser usados diretamente;

