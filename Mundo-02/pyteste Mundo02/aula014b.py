'''for c in range(1, 3):
    n = int(input('Digite um valor: '))
print('Fim')'''

# Considerando processo com uma quantidade não conhecida de entradas:
# Loop sem fim até você digitar 0:
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')

# Pode ser também com string, de forma qu o operador escolha como parar:
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('Fim')