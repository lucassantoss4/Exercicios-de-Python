num =  int(input("Informe um número: "))

for c in range(1,num+1):
    if num % c == 0: 
        print('O número informado é divisivel exato por {}'.format(c)) 
    else:
        print('O número informado é divisivel  não exato por {}'.format(c))


# num = int(input('Digite um número : '))
# for c in range(1,num+1):
#     if num % c ==0:
#         print('\033[34m', end='')
#     else :
#         print('\033[31m', end='')
#      print('{} '.format(c), end='')