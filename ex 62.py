n1 = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão: '))

termo = n1
cont = 1

# k = n1+(9*r)

while cont <= 10:
    print('{} →'.format(termo), end = '')
    termo = termo + r
    cont = cont + 1

print('FIM')