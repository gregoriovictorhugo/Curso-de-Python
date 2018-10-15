frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #Separa em uma lista
junto = ''.join(palavras) #Junta em uma palavra
inverso = ''

for letra in range(len(junto) - 1, -1, -1): # Comprimento da palavra de junto mais um slot, começando pelo 0 e indo de tras para frente
    inverso += junto[letra]

print('O inverso de {} é {}'.format(junto, inverso))

if inverso == junto:
    print('É um palíndromo!')

else:
    print('NÃO é um palíndromo')


