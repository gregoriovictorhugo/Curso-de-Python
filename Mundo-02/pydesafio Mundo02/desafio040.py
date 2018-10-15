nota1 = float(input('Digite sua nota na primeira unidade: '))
nota2 = float(input('Digite sua nota na segunda unidade: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('-=-'*20)
    print('A média do aluno foi: {}'.format(media))
    print('O aluno foi REPROVADO')

elif 5 >= media or media <= 6.9:
    print('-=-'*20)
    print('A média do aluno foi: {}'.format(media))
    print('O aluno vai para a recuperação')

elif media >= 7:
    print('-=-'*20)
    print('A média do aluno foi: {}'.format(media))
    print('O aluno foi APROVADO')