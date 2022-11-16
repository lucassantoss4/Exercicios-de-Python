n1 = int(input('Digite um numero: '))
n2 = int(input('Escolha mais um número: '))

div = n1/n2


if div > 1:
    print('O primeiro valor é o maior,{} > {}'.format(n1,n2))
elif div == 1:
    print('Não existe valor maior, os dois são iguais')
else:
    print('O segundo é maior')