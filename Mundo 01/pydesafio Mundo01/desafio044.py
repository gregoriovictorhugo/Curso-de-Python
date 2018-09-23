valor = float(input('Digite o valor do produto: '))
pagamento = int(input(''' 
[1] DINHEIRO/CHEQUE
[2] CARTÃO
[3] 2X NO CARTÃO
[4] 3X OU MAIS
Digite a forma de pagamento: '''))
print('-=-'*20)

if pagamento == 1:
    print('10% de desconto')
    print('O valor a ser pago pelo produto é: {}'.format(valor - (valor*0.1)))

elif pagamento == 2:
    print('5% de desconto')
    print('O valor a ser pago pelo produto é: {}'.format(valor - (valor * 0.05)))

elif pagamento == 3:
    print('Preço normal')
    print('O valor a ser pago pelo produto é: {}'.format(valor))

elif pagamento == 4:
    print('20% de juros')
    print('O valor a ser pago pelo produto é: {}'.format(valor + (valor * 0.2)))

