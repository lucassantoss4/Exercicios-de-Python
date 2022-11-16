sexo = str(input('Informe o seu sexo [M/F]:  ')).strip().upper()[0] #upper para deixar mau=iuscula e strip para tirar os espacos 

while sexo not in "MnFf" : # enquanto sexo não estiver em "MnFf" ...
    sexo = str(input('Dados invalidos. \nInforme o seu sexo [M/F]:  ')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(sexo))