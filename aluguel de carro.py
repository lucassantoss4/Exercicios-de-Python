km = int(input('Quantos Km percorridos : '))
dias = int(input("Quantos dias foram alugados :"))

valor_dia = dias*60
valor_km = 0.15*km
total = valor_dia + valor_km

print('O total a pagar é de R$:{:.2f}'.format(total))