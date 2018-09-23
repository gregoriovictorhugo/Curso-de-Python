velocidade = int(input('Velocidade do veículo: '))

if velocidade >= 81:
    print('Você ultrapassou o limite de velocidade! A multa vai chegar...')
    multa = 7*(velocidade-80)
    print('O valor da multa será de {} Reais'.format(multa))

else:
    print('Faça sua viagem tranquilo! Você esta na velocidade limite')