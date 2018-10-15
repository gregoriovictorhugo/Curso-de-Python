from time import sleep
print('Progressão aritimética com WHILE')
sleep(1)
print('-=-'*10)
sleep(1)

r = int(input('Digite a razão da PA: '))
p = int(input('Digite o primeiro termo: '))
c = 0
s = p

while c != 10:
    c += 1
    print('Progressão parte {}: {}'.format(c, s))
    s += r
    sleep(1)

print('Fim')
