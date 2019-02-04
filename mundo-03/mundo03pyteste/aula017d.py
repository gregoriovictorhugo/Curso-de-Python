# Relacionando listas:
a = [2, 3, 4, 7]
b = a[:]

# Mandando que b receba uma cópia dos valoes de A:
# É criado uma cópia da lista A, logo alterando os valores de B não interfere nos valores de A
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B:{b}')

# mudando o valor de uma lista relacionanda:
# LISTAS INTERLIGADAS, A ALTERAÇÃO DEU UMA LISTA MUDA A OUTRA
b = a
b[2] = 8
print(f'\nLista A: {a}')
print(f'Lista B:{b}')


