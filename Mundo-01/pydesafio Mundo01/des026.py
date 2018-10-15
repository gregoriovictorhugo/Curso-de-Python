frase = str(input('Digite uma frase: ')).strip().lower()

print('A frase apresenta letra A, {} vezes'.format(frase.count('a')))
print('A primeira letra A aparece na posição: {}'.format(frase.find('a')+1)) #+1 porque o primeiro slot é 0
print('A última vez que a letra A aparece na frase: {}'.format(frase.rfind('a')+1))