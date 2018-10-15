print('Identificação da classe de competição do atleta')
print('-=-'*20)
ano = int(input('Digite o ano de nascimento do atleta: '))

idade = 2018 - ano

if idade <= 9:
    print('Categoria MIRIM')

elif (idade > 9) and (idade <= 14):
    print('Categoria INFANTIL')

elif (idade > 14) and (idade <= 19):
    print('Categoria JUNIOR')

elif idade == 20:
    print('Categoria SÊNIOR')

elif idade > 20:
    print('Categoria MASTER')