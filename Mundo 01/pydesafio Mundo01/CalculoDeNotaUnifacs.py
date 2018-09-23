s_numero = input('Digite um número: ')

if int(s_numero[s_numero.find('.')+1]) >=5:
    print(int(s_numero[:s_numero.find('.')])+1)

else:
    print(s_numero[:s_numero.find('.')])