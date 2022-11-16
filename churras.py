with open ('churras.csv', 'r') as arq:
    items = arq.readlines() # o que é readlines ?

    #print(items)

    total = 0.0
    for item in items:
        colunas = items.strip().split(',') # ei professor o que vc fez aqui ? são duas funcoes ?
        gasto = float(colunas[1]*float(colunas[2]))
        total += gasto

print('{:.2f}'.format(total))