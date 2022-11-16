 # from traceback import print_tb


# from sre_parse import SPECIAL_CHARS


# v_casa = int(input('\nDigite o valor da casa. R$: '))
# salario = int(input('\nDigite o seu salário. R$: '))

# qtd_anos = int(input('\nDigite quantos anos você quer parcelar  '))

# emprestimo = salario*0.3
# parcela = salario*0.3
 
# prestacao = v_casa/salario*(12*qtd_anos)

# if salario > emprestimo:
#     elif parcela < salario:
#         print("pode emprestimo")

# else:


## CORREÇÃO DO GUANABARA
casa = float(input('Valor da casa R$: '))
salario2 = float(input('Salario do comprador R$: '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario2*0.3 # o minimo é 30% do salario 
print('Para pagar uma casa de R$:{:.2f} em {} anos'.format(casa, anos), end='')# end='' é usado para junta a proxima linha na anterior.
print(' a prestação será de R$:{:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO')
else:
    print('Emprestimo NEGADO! ')


