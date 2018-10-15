from time import sleep
print('Somatório de todos os múltiplos de 3 entre 1 e 500')
sleep(1)

s = 0

for c in range(3, 500, 3):
    s += c
    print('Múltiplo: {}'.format(c))
    sleep(1)
    print('Somatório: {}'.format(s))
    sleep(1)
    print('-=-'*10)
    sleep(1)
print('FIM')

