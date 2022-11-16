# from math import factorial
# num = int(input('Digite um número: '))
# fac = factorial(num)
# print('o fatorial de {} é {} '.format(num,fac))





num = int(input('Digite um número : '))
cont = num
multi = 1
while cont > 0 :
    # c = (num - i) 
    print('{}'.format(cont), end='')
    print(" x " if cont > 1 else ' = ', end = '')
    multi = multi * cont
    cont -= 1
print('{}'.format(multi))