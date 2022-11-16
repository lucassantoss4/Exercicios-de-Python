frase = str(input("Digite uma frase: "))
maiuscula = frase.upper()
encontrar = maiuscula.count("A")
posicao = (frase.find("A")+1)

print (" A letra A apareceu {} vezes na frase.".format(encontrar))
print (" A primeira letra A Apareceu na posição {}".format(posicao))
