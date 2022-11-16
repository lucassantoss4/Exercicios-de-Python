nome = input("Qual é o seu nome completo: ")


capitalize = nome.capitalize()
lista_nome = capitalize.split()

if 'Silva' in lista_nome :
    print('Seu nome tem Silva ? sim')

else:
    print('Seu nome tem Silva ? não')