listanum = []
maior = 0
menor = 0

for c in range(0, 5):
    listanum.append(int(input(f"Digite um valor para a posição {c}: ")))

    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]

print('-='*30)
print(f'você digitou os valores: {listanum}')
print('-='*30)
print(f'{maior} foi o maior valor declarado')
print(f'{menor} foi o menor valor declarado')






