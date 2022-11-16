velocidade = float(input("Qual a velocidade do Carro : Km "))

if velocidade <= 80 : 
    print ("Não ultrapasse 80 Km/h ")
else:
    multa = (velocidade - 80) * 7
    print("Você será multado em R$:{:.2f}".format(multa))