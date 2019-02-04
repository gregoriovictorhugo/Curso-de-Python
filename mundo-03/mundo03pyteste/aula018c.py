# Criando um lista com outras dentro de forma mais direta:
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

# Criando prints de diferentes dados e infomações presentes na lista
print(galera[0][0])
print(galera[2][1])

# Criando uma lista com os dados declarados
for p in galera:
    print(p)
    # assim ele irá mostrar as pessoas cadastradas (p)
    print(f'{p[0]} tem {p[1]} anos de idade.')