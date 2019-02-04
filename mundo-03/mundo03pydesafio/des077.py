palavras = 'programar', 'code', 'css', 'java', 'python', 'javascript', 'computador', 'engenharia', 'treinar', 'tentar', 'hustle'

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos, ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')