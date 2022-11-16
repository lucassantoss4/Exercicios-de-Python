# s=0
# for c in range(18, 1, -3):
#     num = int(input('Digite um número '))
#     s=s+num 

#     print(c)
# print(s)


# CORREÇÃO DO GUANABARA 
s=0
for c in range(1,501, 2):
    if c % 3 == 0:
        s=s+c
print('A Soma de todos os valores é {}'.format(s))
