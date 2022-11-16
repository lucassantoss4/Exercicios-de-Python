cidade = input("Em qual cidade você nasceu? ")

# criar um 'fúnil' para restar apenas o que quero "SANTO"
maiusculo = cidade.upper() # a palavra fica MAIUSCULA
divir = maiusculo.split() # formar uma lista
separar = divir[0] # pegar so o primeiro nome 
espacos = separar.strip() # titar todos os espacos


if espacos == "SANTO" :
    print ('True')


else:
    print("False")