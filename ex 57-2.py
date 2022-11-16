
sexo = str(input('Qual é o sexo [M/F]: ')).strip().upper()[0]

while sexo not in "mMfF":
    sexo = str(input('Dados invalidos \nQual é o sexo [M/F]: ')).strip().upper()[0]

