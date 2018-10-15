frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O')) #Transforma toda a frase em maiusculo e depois conta os O maiusculo
print(len(frase)) #conta os slots na variavel frase
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print('curso' in frase)
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('curso'))
print(frase.split()) #Forma a lista com um string por palavra

frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[0])


# O uso de spas triplas é para textos grandes, respeitando o espaçamento dado pelo print do texto
print("""Welcome! Are you completely new to programming? about why and how to get started with Python. Fortunately 
an experienced programmer in any rpogrammer language (whatever it may be) can pick up Python very quickly.
Its also easy for beginners to use and learn, so jump in!""")
