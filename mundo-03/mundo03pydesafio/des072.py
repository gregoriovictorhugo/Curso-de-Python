tupla = ('Zero', 'Um', 'Dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
         'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número de 0 a 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {tupla[num]}')
        break
    else:
        print('Valor inválido, digite novamente \n')