l = float(input("Largura da parede: "))
h = float(input("Largura da parede: "))

area = l*h
conversao = (area * 1) / 2

print('Sua parede tem a dimensão de {} x {} e sua área é de {} m². para pintar essa parede, você precisará de {}L de tinta.'.format(l, h, area, conversao))