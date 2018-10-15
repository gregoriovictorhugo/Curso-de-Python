n = c = a = 0
n = int(input('Digite um número: '))
while n != 999:
    c += 1
    a += n
    print('Caso deseje sair do programa digite 999')
    n = int(input('Digite um número: '))

print('Você deu entrada em {} números'.format(c))
print('A soma total dos números digitados é {}'.format(a))

