valores = list()

# Valores da lista declarados pelo operador:
for cont in range(0, 5):
    valores.append(int(input('Digite um número inteiro: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c}, encontrei o valor {v}!')
print('Cheguei ao final da lista.')