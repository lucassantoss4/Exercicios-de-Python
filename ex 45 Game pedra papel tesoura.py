from random import randint
itens = ('Pedra', 'Papel','Tesoura')

cpu_joga = randint(0,2)

print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura ''')
jogador = int(input('Qual é a sua jogada? '))
print('-=-'*20)
print('Computador jogou {}'.format(itens[cpu_joga]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=-'*20)
# print('O computador escolheu {}'.format(itens[cpu_joga]))

if cpu_joga == 0:
    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
    
elif cpu_joga == 1:
    if jogador == 0:
        print('COMPUTADOR GANHA')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR GANHOU')

    else:
        print('JOGADA INVALIDA')

elif cpu_joga == 2:
    if jogador == 0:
        print('JOGADOR GANHOU')
    elif jogador == 1:
        print('COMPUTADOR GANHOU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')
