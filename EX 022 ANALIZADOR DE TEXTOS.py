

nome = str(input("Digite seu nome completo: "))

maiusculas = nome.upper()
minusculas = nome.lower()
tamanho_nome_completo = len(nome)


div = nome.split() 
primeiro_nome = div[0]
tamanho_nome_primeiro = len(primeiro_nome)

print ("Seu nome em maiúsculas é {}".format(maiusculas))
print ("Seu nome em minúsculas é {}".format(minusculas))
print("Seu nome tem ao todo {}".format(tamanho_nome_completo))
print("Seu primeiro nome é {} e ele tem {} letras".format(primeiro_nome, tamanho_nome_primeiro))