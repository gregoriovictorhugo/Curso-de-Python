maior = 0
menos = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1: # Inícialmente o primeiro peso lido se torna maior em menor
        maior = peso
        menor = peso
    else: # Com os outros testes, novos pesos podem assumir os valores de menor ou maior
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
