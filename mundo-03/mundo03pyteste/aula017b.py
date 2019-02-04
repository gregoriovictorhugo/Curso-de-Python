# Criando uma lista vazia
valores = list()
# pode escrever tbm: valores = []

valores.append(5)
valores.append(9)
valores.append(4)

# Forma organizada de ler a lista criada
for c, v in enumerate(valores):
    print(f'Na posição {c}, encontrei o valor {v}!')
print('Cheguei ao final da lista.')
