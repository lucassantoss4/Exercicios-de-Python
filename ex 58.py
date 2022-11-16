import random
sorteador = random.randint(0,10)

while sorteador  != num:
    num =  int(input("Escolha um número de 0 á 10 : "))
    print(sorteador)
    if num > sorteador:
        print('Muito Alto')
        erro = int(input(('n\Tente novamente:')))
    elif num < sorteador:
        print('Muito Baixo')
        erro = int(input('Tente novamete: '))
    elif num == sorteador:
        print('PARABÉNS VOCÉ ACERTOU O NÚMERO SORTEADO !!!')




    # if num == sorteador:
    #         print('PARABÉNS VOCÉ ACERTOU O NÚMERO SORETADO !!!')
    # else:
    #         print('TENTE NOVAMENTE \nEscolha mais um Número: ')