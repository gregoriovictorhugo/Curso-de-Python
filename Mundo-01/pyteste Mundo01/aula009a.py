frase = 'Curso em Vídeo Python'
# Apresenta 20 slots ocupados (de 0 a 20)
frase[9]
frase[9:13]
frase[9:21]
frase[9:21:2]
frase[:5]
frase[15:]
frase[9::3]

# Análise de string:
# Função LEN length (comprimento): Função de análise de string que demonstra o comprimento da frase
len(frase)

# Vai contar quantos 'o' existem na frase
frase.count('o')
# Contar quantos 'o' existem de 0 a 13 (sem contar o slot 13)
frase.count('0', 0, 13)
# .find: para encontrar determinada parte da frase, dizendo onde começa o que procuro (deo começa no slot 11)
frase.find('deo')
# frase.find('android') -- Neste caso a resposta será -1 já que nao ha o string android (posição -1 não existe)

# Operador IN: diz se true or false quanto a existência de uma string
'Curso' in frase

# Operador .REPLACE: Troca a string selecionada por outra
# A substituição nao acontece direta no string
frase.replace('Python', 'Android')

# Operador .UPPER(): Transformaa as letras em maíusculo:
frase.upper()

# Operador .LOWER(): transforma as letras em minúsculo
frase.lower()

# Operador .capitalize(): Torna a primeira letra em maiusculo e as outras letras em minusculo
frase.capitalize()

# Operador .title(): Torna todas as primeiras letras das palavras presentes na frase em maiusculo
frase.title()

# Operador .strip(): Remove todo os espaços inutes presentes em uma frase string (os espaços antes das letras e depois da letra)
frase.strip()
frase.rstrip() #Usado para excluir os espaçõs inutes presentes a direita da frase
frase.lstrip() #Usado para excluir os espaços presentes a esquerda da frase

# Operador .split(): Elimina todos os espaços presentes no string, desta forma separando as palavras em strings diferentes
# Divide a string frase em uma lista de string: no caso estudado (de 0 a 3)
frase.slipt()

#Operador .join(): após usar o slipt este operador vai unir os strings criados pelo slipt
'-'.join(frase)
# O - será usado para unir as string no lugar de espaçamento