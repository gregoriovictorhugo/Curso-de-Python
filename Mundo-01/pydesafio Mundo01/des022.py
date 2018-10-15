nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maíusculas: {}'.format(nome.upper()))
print('Seu nome em minúsculas: {}'.format(nome.lower()))
# Total de letras com espaço - os espacos (- nome.count(' '))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
# Usando o find para encontrar o primeiro espaço existente do nome, ele ira mostrar apenas a quantidade de slots do primeiro nome
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
