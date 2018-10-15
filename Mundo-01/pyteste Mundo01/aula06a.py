n0 = input('digite um número')
print(type(n0))
n0 = float(n0)
print(type(n0))
print(n0)
n0 = bool(n0)
print(type(n0))
print(n0)
n0 = str(n0)
print(n0.isnumeric())

n = input('digite algo: ')
print(n.isnumeric())

n1 = (input('digite um valor: '))
n2 = (input('digite outro valor: '))
s = n1 + n2
print('o valor da som é:', s)
print('a soma ente', n1, 'e', n2, 'é:', s)
print('a soma entre {} e {} vale {}'.format(n1, n2, s))
# por não declarar o número como int, ele segue interpretado como string, logo a soma irá apenas juntas os valores declarados

