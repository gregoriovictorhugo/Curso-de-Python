from time import sleep

print('Tabuada usando o FOR: ')
sleep(1)
print('-=-'*10)
sleep(1)
n = int(input('Digite o número que você deseja saber a tabuada: '))

for c in range(0, 11):
    print('{} x {} = {}'.format(n, c, (n*c)))
    sleep(1)
    print('-'*10)
    sleep(1)
print('Fim')