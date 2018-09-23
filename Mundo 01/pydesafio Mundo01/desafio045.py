from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura') #CRIAÇÃO DE LISTA
computador = randint(0, 2) #ESCOLHA ENTRE OS TRÊS NOMES PRESENTES NA LISTA

print('''
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua escolha? '))

print('-=-'*20)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('-=-'*20)

print('O computador jogou: {}'.format(itens[computador]))
print('O jogador jogou: {}'.format(itens[jogador]))

if computador == 0: #PEDRA
    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
        print('VOCÊ GANHOU!')

    elif jogador == 2:
        print('O COMPUTADOR GANHOU')

    else:
        print('JOGADA INVÁLIDA')

elif computador == 1: #PAPEL
    if jogador == 0:
        print('COMPUTADOR GANHOU')

    elif jogador == 1:
        print('EMPATE')

    elif jogador == 2:
        print('VOCÊ GANHOU')

    else:
        print('JOGADA INVÁLIDA')

elif computador == 2: #TESOURA
    if jogador == 0:
        print('VOCÊ GANHOU')

    elif jogador == 1:
        print('COMPUTADOR GANHOU')

    elif jogador == 2:
        print('EMPATE')

    else:
        print('JOGADA INVÁLIDA')






