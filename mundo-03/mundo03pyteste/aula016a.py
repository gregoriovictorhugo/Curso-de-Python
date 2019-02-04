# Tuplas utilizam ()
lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim')

print(lanche)# Mostra todas as variáveis da tupla
print(lanche[1])# Suco
print(lanche[3])# Pudim
print(lanche[-2])# Pizza
print(lanche[1:3])# Suco, Pizza (Desconsidera o último sempre)
print(lanche[:2])# Mostra do nício ate o elemento 2, ignorando este elemento
print(lanche[-3:])# Suco, Pizza, Pudim
print(len(lanche))# Mostra quantas variáveis cadastradas

# Tuplas são imutáveis
 # lanche[1] = 'Refrigerante'
 # print(lanche[1])# Vai dar erro


# Melhor estilização da tupla:
 # Caso nao precise da posição das variáveis:
for comida in lanche:
    print (f'Eu vou comer {comida}')
print('Comi pra caramba!')

print('\n', '-=-'*10, '\n')

 # Caso precise da posição das variáveis
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi pra caramba!')

print('\n', '-=-'*10, '\n')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba')

 # Usando o enumerate ele disponibiliza a variável e sua posição
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('\n', '-=-'*10, '\n')
#ORGANIZANDO A TUPLA EM ORDEM:
print(sorted(lanche))