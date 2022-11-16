# Lendo de linha em linha (note o plural em readlines)
with open('texto-cancao.txt', 'r') as arquivo:
    # linhas é uma lista de strings, cada linha é uma string diferente
    linhas = arquivo.readlines()
    # Verificando que linhas é uma lista de strings
    print(linhas)
    # Imprimindo de linha em linha
    for linha in linhas:
        print(linha)