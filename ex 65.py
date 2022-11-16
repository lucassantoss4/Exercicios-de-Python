# num = 0

contador = 0
maior_valor =0
menor_valor =0
num = int(input("Digite um número: "))
soma = num

continuar = True
while continuar:
    num = int(input("Digite um número: "))
    if contador == 1:
        maior_valor = menor_valor = num
    else:
        if num > maior_valor:
            maior_valor = num
        elif num < menor_valor:
            menor_valor = num
    soma += num
    contador += 1
    media = num/contador
    continuar = str(input('Deseja continuar ? [S/N] : ')).upper().strip()[0]
    if continuar == 'N' or 'n':
        continuar = False
        print('a soma é {} e a media dos seus valores é {}'.format(soma,media))

print('O menor valor é {} e o maior valor é {}'.format(menor_valor,maior_valor))