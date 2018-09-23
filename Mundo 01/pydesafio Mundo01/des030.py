n = int(input('Digite um número aqui: '))
print('Vamos ver se este numéro é PAR ou ímpar...')
print('-=-'*20)

resto = n % 2 # Operação para encontrar o resto da divisão completa de n

if resto == 0:
    print('{} é PAR!'.format(n))

else:
    print('{} é ÍMPAR!'.format(n))