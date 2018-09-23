nome = input('qual é o seu nome? ')
print('Prazer em teconhecer, {}!'.format(nome))
print('Prazer em teconhecer, {:=^20}!'.format(nome)) # alinha no centro dos simbolos
print('Prazer em teconhecer, {:<20}!'.format(nome)) # alinha a esquerda
print('Prazer em teconhecer, {:>20}!'.format(nome)) # alinha a direita

n1 = int(input('um valor: '))
n2 = int(input('outro valor: '))
print('A soma vale {}'.format(n1 + n2))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print ('a soma é {}, o produto é {} e a divisão é {}'.format(s, m, d))
print ('Divisão inteira {} e poténcia {}'.format(di, e))