nome = str(input("Digite seu nome completo: "))
lista_nome = nome.split()
primeiro_nome = lista_nome[0]
ultimo_nome = [len(nome)]-1
print("Seu primeiro nome é {}".format(primeiro_nome))
# print("Seu último nome é {}".format(ultimo_nome))
print("Seu último nome é {}".format(nome[len(nome)]-1))