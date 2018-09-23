n = int(input('digite um número: '))
u = n // 1 % 10 #Divisão total por 1 (o numero em si), logo dividir o resultado por 10 e declarar seu ultimo resto (Por ser int, numeros apos o . sãp desconsiderados
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidade: {}'.format(n[u]))
print('Dezena: {}'.format(n[d]))
print('Centena: {}'.format(n[c]))
print('Milhar: {}'.format(n[m]))