print('Olá! Vou analisar a possibilidade do seu emp´restimo bancário.')
print('-=-'*20)

valor = float(input('Digite o valor do imóvel: '))
salario = float(input('Digite o valor do seu salário: '))
anos = int(input('Digite em quantos anos pretende pagar o imóvel: '))

prestacao = valor / (anos * 12)

if prestacao < (salario*0.3):
    print('Em {} anos, o valor da prestação será de {:.2f}'.format(anos, prestacao))
    print('Lembrando que o valor esta sujeito a reajuste')

elif prestacao >= (salario*0.3):
    print('Desculpe mas o emprestimo não é permitido, tente aumentar os anos de prestação')