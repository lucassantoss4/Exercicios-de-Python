frase = 'Curso em Video Python'
frase2 = "     Aprendar Python    "
## analise
fra = frase[9::3]#começa em 9 pela de 3 em 3 /recorte
tamanho = len(frase)
contar = frase.count('o') # serve para contar quantos "o" tem seja "o" qualquer coisa
encontrar = frase.find("deo") # indica a posição do que voce procura, que no casa é 'deo'

## tranformação
substtuir = frase.replace('Python', "Android")
maiusculo = frase.upper()
minusculo = frase.lower()
capitalize = frase.capitalize()
capitalize_por_palavra = frase.title()
remove_espacos_inuteis = frase2.strip() # remove os espaços
remove_espacos_inuteis_r = frase2.rstrip()# remove os espaços da direita
remove_espacos_inuteis_l = frase2.lstrip() # remove os espaços da esquerda

## divisão
div = frase.split() #faz uma divisão onde tem espaços  
juncao = '-'.join(frase) # o que vc quiser ele junta e coloca a informação que esta entre aspas "-"



print(fra)
print(tamanho)
print(contar)
print(encontrar)
print(frase)
print(maiusculo)
print(minusculo)
print(capitalize)
print(capitalize_por_palavra)
print(remove_espacos_inuteis)
print(remove_espacos_inuteis_r)
print(remove_espacos_inuteis_l)
print(div)
print(juncao)