tabela = ('palmeiras', 'flamengo', 'internacional', 'são paulo', 'grêmio', 'atlético', 'santos', 'atlético-pr', 'cruzeiro',
          'fluminense', 'corinthians', 'vasco da gama', 'bahia', 'ceará SC', 'botafogo', 'américa-MG', 'chapecoense',
          'sport recife', 'vitória', 'paraná')

while True:
    opcao = str(input('''Digite a opção desejada:
    [A] 5 Primeiros colocados
    [B] 4 Ultimos colocados
    [C] Ordem alfabética
    [D] Posição da chapeco
    Opção: ''')).lower()

    if opcao == 'a':
        print(tabela[0:5])
        break

    if opcao == 'b':
        print(tabela[-4:])
        break

    if opcao == 'c':
        print(sorted(tabela))
        break

    if opcao == 'd':
        print(f'O Chapeco está na {tabela.index("chapecoense")} posição')
        break

    else:
        print('Opção inválida, tente novamente. \n')
