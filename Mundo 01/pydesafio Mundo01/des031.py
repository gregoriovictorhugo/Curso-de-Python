distancia = float(input('Digite a distância da viagem em quilômetros: '))

if distancia >= 201:
    valor = ((200 * 0.5) + ((distancia - 200) * 0.45))
    print('-=-'*20)
    print('A passagem irá custar {} reais'.format(valor))

else:
    valor = (distancia*0.5)
    print('-=-'*20)
    print('A passagem irá custar {}'.format(valor))

