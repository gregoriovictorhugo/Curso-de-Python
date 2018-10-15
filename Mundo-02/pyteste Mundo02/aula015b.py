# Usando comandos de fstrings (versão python 3.6)
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# print('A soma vale {}'.format(s))
# O f acaba por interpolar as variáveis, desta forma a mesma pode ser atribuída diretamente
print(f'A soma vale {s}')