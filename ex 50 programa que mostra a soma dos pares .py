s=0
contador = 0
for c in range(1,7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        s = s+num
        contador = contador + 1

print('Você informou {} números PARES e a soma foi {}'.format(contador,s))