num = input("Digite um número: ")

divid = num.split()

milhar = divid[0][0]
centena = divid[0][1]
dezena = divid[0][2]
unidade = divid[0][3]


print("Analisando o número: {} Unidade: {}, Dezena: {}, Centena: {}, Milhar: {} ".format(num, unidade, dezena, centena, milhar))