lista = ('Lápis', 1.75,
        'Borracha', 2,
        'Caderno', 15.90,
        'Estojo', 25,
        'Transferidor', 4.20,
        'Compasso', 9.99,
        'Mochila', 120.32,
        'Canetas', 22.30,
        'Livros', 34.90)

print('-' * 20)
print('LISTAGEM DE PREÇOS')
print('-' * 20)
for pos in range(0, len(lista)):

    if pos % 2 == 0: #Para nome,s estam em posição par
        print(f'{lista[pos]:.<30}', end='')
    else: #Para preços, estão em posição ímpar
        print(f'R$ {lista[pos]}')
