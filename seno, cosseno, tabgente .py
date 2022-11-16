import math 

angulo =float(input("Digite o ângulo que você deseja: "))
seno = math.sin(math.radians(angulo))
coss = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print ('O ângulo de {} tem o seno de: {:.2f}, cosseno de: {:.2f}, e tângente: {:.2f} '.format(angulo, seno, coss, tang))