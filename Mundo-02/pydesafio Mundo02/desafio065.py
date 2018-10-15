media = maior = c = a = n = 0
opcao = 'Y'

while opcao != 'N':
    n = int(input('Digite um número: '))
    c += 1
    a += n
    media = a / c
    if maior < n:
        maior = n
    opcao = str(input('Deseja continuar a declarar valores? [Y/N]')).upper()

print('O maior número digitado foi {}, sendo a média de todos os números declarados igual a {}'.format(maior, media))

