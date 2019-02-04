
n = int(input('Digite um número: ')), /int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')), int(input('Digite o  ultimo número: '))

print('-=-'*10)
print(f'[A] O número nove foi digitado {n.count(9)} vezes\n')
if 3 in n:
    print(f'[B] O número 3 foi digitado na posição {n.index(3)+1}')
else:
    print('Não há número 3 declarado')
print(f'O valores pares digitados foram: ')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')


