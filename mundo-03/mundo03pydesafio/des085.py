num = [[], []]

valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o valor: '))

    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print('-=-'*30)
print(f'Valores pares: {num[0]}')
print(f'Valores ímpares: {num[1]}')
