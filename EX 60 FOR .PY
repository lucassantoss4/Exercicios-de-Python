num = int(input('Digite um número: '))
i = 0
ca = num
multi = 1
for c in range(num,i,-1):
    # print('{} x '.format(c), end='')
    print('{} x '.format(c) if c > 1 else ' = ', end='')
    ca -=1
    multi = multi * c

print(multi)




n = int(input('Digite u mnúmero para ver seu fatorial: '))
c = n
f = 1
print(f'Calculando... {n}', end='')
for fat in range(n, 0, -1):
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
    f *= fat
print(f'{f}')