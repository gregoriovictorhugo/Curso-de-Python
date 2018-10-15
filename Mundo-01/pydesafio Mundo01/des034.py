salario = float(input('Digite seu salário: '))
print('Calculando seu aumento...')
print('-=-'*20)

if salario <= 1250:
    aumento = 1.15*salario
    print('Com o aumento de 15% seu novo salário será de: {:.2f}'.format(aumento))

else:
    aumento = 1.10*salario
    print('Com o aumento de 10% seu novo salário será de: {:.2f}'.format(aumento))