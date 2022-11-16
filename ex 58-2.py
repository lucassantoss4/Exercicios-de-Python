import random

sorteador = random.randint(0,10)


tentativas = 0
acertou = False
while not acertou :
    num = int(input('Escolha um número: '))
    tentativas +=1
    if num == sorteador:
        print("VoCÊ acertou com {} tentativas".format(tentativas))
        acertou = True
    elif num > sorteador:
        print('Maior \nchute um número menor')
    elif num < sorteador:
        print('Menor \nchute um número maior')

        
print(sorteador)