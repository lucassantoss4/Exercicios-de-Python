a1 = int(input("Qual é o primeiro TERMO da sua P.A: "))
r = int(input("Qual é a RAZÃO da sua P.A: "))

cont=0
for c in range(a1,a1+10*r,r):
    print("{}".format(c), end=' → ')
    # formula = a1*r
    cont = cont +1
    # print("pa {} e contador{}".format(c,cont))

print('ACABOU')

