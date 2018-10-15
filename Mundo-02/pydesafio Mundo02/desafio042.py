print('Vamos tentar formar um triângulo com três retas!')
print('-=-'*20)

print('Digite os comprimentos das três retas: ')
r1 = float(input('reta 1: '))
r2 = float(input('reta 2: '))
r3 = float(input('reta 3: '))

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('É possível formar um triângulo com as retas')

    if r1 == r2 == r3:
        print('Triângulo equilátero')

    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Triângulo Isóceles')

    else:
        print('Triângulo Escaleno')


else:
    print('Não é possível formar um triângulo com as retas')

