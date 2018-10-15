from random import randint

n = randint(0, 5)

print('-=-'*20)
print('Vou pensar em um número de 0 á 5...')
print('-=-'*20)

c = int(input('Em que número eu pensei? '))

if n == c:
    print('Parabéns, você acertou!')
else:
    print('Eu pensei no número {} e não no {}, tente de novo!'.format(n, c))