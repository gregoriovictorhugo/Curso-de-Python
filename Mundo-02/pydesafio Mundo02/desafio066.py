s = cont = 0
while True:
    n = int(input('Digite um número inteiro: (999 para parar) '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Foram digitados {cont} números, sendo a soma entre eles igual a {s}.')