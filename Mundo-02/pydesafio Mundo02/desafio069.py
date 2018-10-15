cont = cont1 = cont2 = 0
while True:
    print('-=-'*10)
    print('Cadastro pessoal:')
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [h/m]: ')).lower()
    opcao = str(input('Digite n para interromper programa: ')).lower()
    if idade > 18:
        cont += 1
    if sexo == 'h':
        cont1 += 1
    if sexo == 'm' and idade < 20:
        cont2 += 1
    if opcao == 'n':
        break
print(f'''
[A] {cont} pessoas tem mais de 18 anos
[B] {cont1} homens foram cadastrados
[C] {cont2} mulheres tem menos de 20 anos''')



