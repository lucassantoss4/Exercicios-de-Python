num = input('Digite um número de 0 á 9999: ')
div = num.split()

milhar = div[0][0]
centena = div[0][1]
dezena = div[0][2]
unidade = div[0][3]


print('unidade: {}, dezena: {}, centena: {}, milhar: {}'.format(unidade, dezena, centena, milhar))