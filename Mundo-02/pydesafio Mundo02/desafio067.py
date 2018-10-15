cont = 0
while True:
    n = int(input('\nDigite um número para saber sua tabuada: (Número negativo para interromper o programa) '))
    if n < 0:
        break
    while cont < 11:
        cont += 1
        resp = n*cont
        print(f'{n} x {cont} = {resp}', ' || ', end='')
print('Fim do programa.')