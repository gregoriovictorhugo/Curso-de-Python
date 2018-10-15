print('Teste de IMC')
print('-=-'*20)

peso = float(input('Digite seu peso em quilogramas: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('-=-' * 20)
    print('Seu IMC é de: {:.2f}'.format(imc))
    print('ABAIXO DO PESO')

elif (imc >= 18.5) and (imc <= 25):
    print('-=-' * 20)
    print('Seu IMC é de: {:.2f}'.format(imc))
    print('PESO IDEAL')

elif (imc > 25) and (imc <= 30):
    print('-=-' * 20)
    print('Seu IMC é de: {:.2f}'.format(imc))
    print('SOBREPESO')

elif (imc > 30) and (imc <= 40):
    print('-=-' * 20)
    print('Seu IMC é de: {:.2f}'.format(imc))
    print('OBESIDADE')

elif imc > 40:
    print('-=-' * 20)
    print('Seu IMC é de: {:.2f}'.format(imc))
    print('OBESIDADE MÓRBIDA')