preco = float(input('Qual é o preço do produto ? R$: '))

desconto = preco*(5/100)
valor = preco-desconto

print('O produto que custava R$:{:.2f}, na promoção com desconto de 5% vai custar R$:{:.2f}'.format(preco, valor))