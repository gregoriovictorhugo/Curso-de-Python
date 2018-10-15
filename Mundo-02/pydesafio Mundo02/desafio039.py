print('Sabe se você precisa se alistar? Consulte aqui!')
print('-=-'*20)
ano = int(input('Digite aqui seu ano de nascimento: '))

idade = 2018 - ano

if idade < 18:
    print('Você ainda não está em idade para se alistar!')
    print('Faltam {} anos para você se alistar'.format(18-idade))

elif idade == 18:
    print('Você já pode se alistar!')

elif idade > 18:
    print('Você já pasou da diade para se alistar!')
    print('Você está {} anos atrasado'.format(idade - 18))