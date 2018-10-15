s = cont1 = 0
menor = ''
men = 999999999999999999999999999
while True:
    print('-=-'*10)
    print('CADASTRO DE COMPRA')
    nome = str(input('Nome do produto: ')).lower()
    preco = int(input('Digite o preço do produto: '))
    opcao = str(input('Para interromper o cadastro digite n: '))
    s += preco
    if preco >= 1000:
        cont1 += 1
    if men > preco:
        men = preco
        menor = nome
    if opcao == 'n':
        break
print(f'''
[A]  Soma dos preços: R$ {s}
[B] {cont1} Produtos custam mais de 1000 reais
[C] {menor} é o produto mais barato''')
