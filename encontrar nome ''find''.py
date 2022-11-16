nome = input('Qual é o seu nome completo? ')

encontrar = nome.find('silva')

if encontrar == -1 :
    print('seu nome não tem silva')

else:
    print("seu nome tem silva. posiçaõ {}".format(encontrar))