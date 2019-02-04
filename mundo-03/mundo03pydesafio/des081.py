lista = []
num = 0

for c in range(0, 5):
    n = int(input('Digite um número para adicionar a lista: '))
    lista.append(n)
    num += 1


print('-=-'*30)
print(f'Os valores digitados foram: {lista}')
print('-=-'*30)
lista.sort(reverse=True)
print(f'Em ordem decrescente: {lista}')
print('-=-'*30)
print(f'Foram digitados {len(lista)} números')
print('-=-'*30)

if 5 in lista:
    print('O número 5 está presente na lista')
else:
    print('O número 5 não está presente na lista')


