frase= ('curso em video python')

novo =frase[9:] # do 9 ate o final
print(novo)

velho = frase [:14] # do começo ate o 14
print (velho)

an = frase [:6] # do comelo ate o dois
print (an)

ar = frase [0:21:2] # começo ate o final de 2 em 2
print (ar)

tr = frase [::2] # mostra o começo e o final pulandop de dois em dois 
print (tr)

po = frase [2::4] #mostra da posisão 2 ate o final pulando de 4 em 4
print (po)

# O find mostra em qual momento começou a letra 

ui = frase.find('louco') #mostra -1 se a busca não estiver na lista 
print (ui)

pi = frase.find('p') #mostra a posicao do p na lista
print (pi)

# COuNT mostra a quantidade de ocorrencias de um determinado "X"/ letra 

we = frase.count('o',0,21) # mostrou a quantidade de o na lista 
print (we)

tf = frase.count("i",0,6) # mostropu 0
print (tf)

# SUBISTITUIR A FRASE POR OUTRA REPLACE
gh = frase.replace('python','lula') # substitui a frase 
print (gh)

#  DEIXA A FRASE EM MAIUSCULO 

fr = frase.upper()
print (fr)

# deixa a frase em minusculo 

ju = frase.lower()
print (ju)

# só o primeiro termo em maiusculo 

re = frase.capitalize()
print (re)

# colocar as primeiras letras em maiusculo 

te = frase.title()
print(te)

# remove os espaços no começo e no final 

frase2 = ( '  eu sou o gustavo!     ')

ga = frase2.strip()
print(ga)

#remover so os utimos espaços

pu = frase2.rstrip()
print (pu)

# remove os espaços no começo
fu = frase2.lstrip()
print (fu)

# cria listas com as palavras 
#tai = []
ou = frase.split()
#tai.append(ou)
print(ou)

#junta palavras por "-" c-u-r-s-o- -e-m- -v-i-d-e-o- -p-y-t-h-o-n

tr = '-'.join(frase)
print(tr)