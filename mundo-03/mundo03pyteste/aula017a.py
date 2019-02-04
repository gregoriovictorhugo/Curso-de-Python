# num = (2, 5, 9, 1) Tupla: IMUTÁVEL

num = [2, 5, 9, 1] #Lista: MUTÁVEL
num[2] = 3
print(num)

# num[4] = 7 Vai dar erro adicionar valores assim, logo deve-se utilizar:
num.append(7) #Adicionando valro 7 ao append
print(num)

# Colocando em ordem crescente:
num.sort()
print(num)
# Colocando em ordem decrescente:
num.sort(reverse=True)
print(num)

# Contando elementos da lista:
# Função len
print(f'Essa lista tem {len(num)} elementos.')

# Adicionando valores a lista:
num.insert(2, 0) #Adicionar 0 na posição 2 da lista!
print(num)

# Remoção de elementos:
num.pop(2) #Elimina o elemento 2 da lista
print(num)
# OBSERVAÇÃO: Caso haja dois elemenots iguais, o pycharm irá varrer a lita do início (posição 0), eliminando apenas o primeiro valor encontrado.
# É possível realizar a remoção de todos os elementos iguais presentes na lista utiliando dos laços.

# Remoção de elementos não existentes na lista
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
