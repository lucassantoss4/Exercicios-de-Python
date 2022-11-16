from datetime import date 
atual = date.today().year
totalmenor = 0
totalmaior = 0
for c in range(1,8):
    ano = int(input('Digite o ano do seu nascimento: '))
    idade = 2022-ano
    # print('Essa pessoa tem {} anos '.format(idade))
    if idade >= 18:
        # print("Velho")
        totalmaior +=1
    else:
        # print('Novo')
        totalmenor +=1

print('total de maiores é {}, e o total de menores é {}'.format(totalmaior,totalmenor))

