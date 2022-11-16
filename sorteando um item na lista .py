import random 

n1= str(input('Digite primeiro aluno: '))
n2 = str(input('Digite segundo aluno: '))
n3 = str(input('Digite terceiro aluno: '))
n4 = str(input('Digite quarto aluno: '))

lista = [ n1, n2, n3, n4]

escolhido = random.choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))