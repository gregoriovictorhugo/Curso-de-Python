n = str(input('Digite um nome: ')).strip()
nome = n.split()
# Nome é a variavel atribuida para a lista criada e n para a frase

print('Primeiro nome: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[len(nome)-1]))