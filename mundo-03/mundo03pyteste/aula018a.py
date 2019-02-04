# Lista dentro de lista
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)
print(galera)

# Mudando variáveis da lista dentro de outra lista
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)
# Ocorre a repetição de maria nos dois slots de galera. Para que não ocorra é necessário uma cópia



