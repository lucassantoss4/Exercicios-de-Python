menor_idade = 0
maior_idade = 0
soma_idade = 0
nome_mais_velho = ''
qtd = int(input('Digite a quantidade de nomes você deseja analisar: '))
for pessoa in range(1,qtd+1):
    nome = str(input('Nome da {}° pessoa: '.format(pessoa)))
    idade = int(input("Idade da {}° pessoa: ".format(pessoa)))
    if pessoa == 1:
        menor_idade = pessoa 
        maior_idade = pessoa
        nome_mais_velho = nome

    else :
        if idade > maior_idade:
            maior_idade = idade
            nome_mais_velho = nome
        if idade < menor_idade: 
            menor_idade = idade
    
    sexo = input('Sexo da {}° pessoa: [M,F]: '.format(pessoa)).strip()
    soma_idade = soma_idade + idade

    media_idade = soma_idade/qtd

# print(media_idade)
# print(maior_idade)
# print(nome_mais_velho)
print('A idade média das pessoas analisada é: {}'.format(media_idade))
print('A pessoa mais velha análisado foi {} com {} anos.'.format(nome_mais_velho, maior_idade))
