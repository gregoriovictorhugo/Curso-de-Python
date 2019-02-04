from random import randint
numeros = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)

print(f'Os núemros sorteados foram: \n')
for n in numeros:
    print(f'{n}', end=' ')

print(f'\nO maior número sorteado foi: {max(numeros)}\n')
print(f'O menor número sorteado foi: {min(numeros)}')


