numeros = []

while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não será adicionado')

    r = str(input('Deseja continuar? [Y/N] '))
    if r in 'Nn':
        numeros.sort()
        print(f'Você digitou os valores: {numeros}')
        break





