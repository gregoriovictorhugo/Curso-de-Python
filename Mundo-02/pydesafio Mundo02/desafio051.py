from time import sleep
print('Progressão aritimética com FOR')
sleep(1)
print('-=-'*10)
sleep(1)

r = int(input('Digite a razão da PA: '))
p = int(input('Digite o primeiro termo: '))
s = 0

for c in range(1, 11):
    if c == 1:
        s = p
        print('Progressão parte {}: {}'. format(c, s))
        sleep(1)
        print('-=-'*10)
        sleep(1)
    else:
        s += r
        print('Progressão parte {}: {}'.format(c, s))
        sleep(1)
        print('-=-' * 10)
        sleep(1)
print('Fim')
