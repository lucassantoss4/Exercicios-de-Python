maior_kg = 0
menor_kg = 0
for pessoa in range(1,6):
    peso = float(input('Peso da {}° pessoa : '.format(pessoa)))
    if pessoa ==1 :
        maior_kg = pessoa
        menor_kg = pessoa
    else:
        if peso > maior_kg:
            maior_kg = peso
        if peso < maior_kg :
            menor_kg = peso

print('O maior peso lido foi de {} Kg \nO menor peso lido foi de {} Kg'.format(maior_kg,menor_kg))