velocidade = int(input('Digite sua velocidade: '))

multa =   (velocidade - 80) * 7

if velocidade <= 80 :
    print(' Tenha um bom dia! Dirija com segurança! ')
else: 
    print('\nMULTADO! Você excedeu o limite permitido de 80 Km/h ')
    print('\nVocê deve paguar uma multa de {}'.format(multa)) 