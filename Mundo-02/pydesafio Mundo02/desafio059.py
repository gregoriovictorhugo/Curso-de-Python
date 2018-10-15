from time import sleep
opcao = 0
print('Bem vindo a calculadora!!!')
print('-=-'*20)

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

while opcao != 5:
    print('''Menu:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')

    opcao = int(input('Digite Sua opção: '))

    if opcao == 1:
        soma = n1 + n2
        print('{} + {} = {} '.format(n1, n2, soma))
        sleep(1)
    elif opcao == 2:
        multi = n1 * n2
        print('{} x {} = {:.2f}'.format(n1, n2, multi))
        sleep(1)
    elif opcao == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
            sleep(1)
        elif n2 > n1:
            print('{} é maior que {}')
            sleep(1)
        else:
            print('Os números são iguais.')
            sleep(1)
    elif opcao == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
        sleep(1)
    elif opcao == 5:
        print('Até a próxima!')
        sleep(1)
    else:
        print('Opção inválida')
        sleep(1)




