n = input('Deseja acessas uma tabuada ?')


if n == 'sim' :
    tabuada = int(input('Qual tabuada deseja acessar ?'))
    
    for i in range(0,11):
        print( "{} x {} = {}".format(tabuada, i, tabuada*i))

else:
    print('Obrigado, Até logo.')