import math
# from math import sqrt
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raíz de {} é igual a {}'.format(num, math.ceil(raiz)))
print('A raíz de {} é igual a {}'.format(num, math.floor(raiz)))
print('A raíz de {} é igual a {:.2f}'.format(num, math.floor(raiz)))