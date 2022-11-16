
num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))



sair = False
while not sair:
    print('+=+='*20)
    menu = print('[1]somar \n[2]multiplicar \n[3]maior \n[4]novos números \n[5]sair do programa')
    operacao = int(input('Escolha uma Opcão: '))
    print('+=+='*20)
    if operacao == 1:
        s = num1+num2
        print('A soma é = {}'.format(s))
    elif operacao == 2:
        mult = num1*num2
        print('A multiplicaçâo é = {}'.format(mult))
    elif operacao ==3:
        if num1 > num2 :
            print('O maior número é {}'.format(num1))
        else:
            print('O maior número é {}'.format(num2))

    elif operacao ==4:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite um número: '))

    elif operacao == 5:
        sair = True  