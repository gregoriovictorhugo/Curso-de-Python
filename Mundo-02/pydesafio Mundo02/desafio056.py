somaidade = 0
mediaidade = 0
maiorhomem = 0
nomevelho = ''
totalmulher20 = 0
for c in range (1, 5):
    print('-=-'*10)
    print('{} pessoa'.format(c))
    nome = str(input('Nome: '.strip()))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '.strip()))
    somaidade += idade

    if c == 1 and sexo in 'Mm':
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome

    if sexo in 'Ff' and idade < 20:
        totalmulher20 += 1

mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorhomem, nomevelho))
print('Ao todo {} mulheres estão com menos de 20 anos'.format(totalmulher20))

