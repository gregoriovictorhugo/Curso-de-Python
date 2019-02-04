lista = []
lista1 = []
lista2 = []

for c in range(0, 5):
    n = int(input(f'Adicione um número a lista: '))
    lista.append(n)

    if (n % 2) == 0:
        lista1.append(n)
    else:
        lista2.append(n)

print('-=-'*10)
print(f'Você digitou: {lista}')
print(f'Os números pares digitados são: {lista1}')
print(f'Os números ímpares digitados são: {lista2}')

