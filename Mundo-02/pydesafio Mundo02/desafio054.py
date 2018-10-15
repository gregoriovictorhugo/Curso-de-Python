n = 0
for c in range(0, 6):
    ano = int(input('Digite o ano em que você nasceu: '))
    idade = 2018 - ano
    if idade < 21:
        n += 1

print('{} pessoa(s) ainda não é/são maior de idade'.format(n))