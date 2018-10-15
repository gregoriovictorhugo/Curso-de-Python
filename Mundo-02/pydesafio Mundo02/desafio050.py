from time import sleep
print('Somatório dos números inteiros')
sleep(1)
print('-=-'*10)
sleep(1)

s = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))
    if (n % 2) == 0:
        s += n
print('O somatório dos números pares digitados é: {}'.format(s))



