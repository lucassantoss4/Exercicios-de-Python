# num = int(input('Digite um número: '))

# contador = 0
# soma = 0

# continuar = True 
# while continuar: 
#     n = int(input('Digite mais um nùmero: '))
#     print('[999] para sair.')
#     contador = contador + 1
#     soma = soma + n
#     if n == 999: 
#         continuar = False

# print('Você digitou {} números \nA soma dos númeos são: {}'.format(contador,soma))

contador = 0
soma = 0
num = 0
num = int(input('Digite mais um nùmero [999] para sair : '))
while num != 999:
    soma = soma + num
    contador = contador + 1
    num = int(input('Digite mais um nùmero [999] para sair : '))
    # if num == 999:
    #     continuar = False


print('Você digitou {} números \nA soma dos númeos são: {}'.format(contador,soma))

