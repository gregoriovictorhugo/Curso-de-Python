from random import randint

computador = randint(0, 5)
i = 0
print('Será que você consegue adivinhar em que número estou pensando?')
chute = int(input('Chute um valor de 0 a 5: '))

while chute != computador:
    print('Você errou!')
    print('-=-'*10)
    i += 1
    chute = int(input('Tente novamente: '))

    if chute == computador:
        print('Parabéns, você acertou!')
        i += 1

print('Você acertou na {}ª tentativa'.format(i))