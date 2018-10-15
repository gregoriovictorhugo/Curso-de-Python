from random import randint
from time import sleep
cont = 0
print('Vamos jogar Par ou ímpar!')
print('-=-'*10)
while True:
    escolha = str(input('Par ou ímpar? ')).upper()
    num = int(input('Escolha um número de 0 a 10: '))
    n = randint(1, 10)
    print(f'Você escolheu {num}')
    sleep(1)
    print(f'O computador escolheu {n}')
    sleep(1)
    if 1 <= n <= 10:
        if escolha == 'PAR':
            resp = n + num
            if (resp % 2) == 0:
                cont += 1
                print('Parabéns, você ganhou!')
            else:
                break
        if escolha == 'IMPAR':
            resp = n + num
            if (resp % 2) != 0:
                cont += 1
                print('Parabéns, você ganhou!')
            else:
                break
        else:
            print('Opção inválida, tente novamente.')
    else:
        print('Número inválido, por favor tente novamente.')
sleep(1)
print(f'Ops, você errou! A soma dos números foi {resp}')
sleep(1)
print(f'Você ganhou {cont} partidas.')