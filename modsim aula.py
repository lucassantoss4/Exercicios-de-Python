# Definição dos parâmetros
ya = 0           # altura do anél
h = 0.1          # altura em metros
yb = h           # altura da barra
va = 0           # velocidade anél
vb = 0           # velocidade da barra 
g= 9.81          # Acel. da grávidade m/s²
ma = 0.01        # massa do anél Kg
mb = 0.08        # massa da barra Kg

ra = 0.05        # raio do anél metros
rb = 0.005       # raio da barra metros 
l0 = 0.04        # complimento inicíal metros
k = 3            # constate da mola N/m 


raiz_1 = (((ra-rb)**2+(yb-ya)**2)**(1/2)-l0)*((yb - ya)/((ra-rb)**2+(yb-ya)**2)**(1/2))
raiz_2 = ((ra-rb)**2+(yb-ya)**2)**(1/2)
delta_y = yb - ya

kl = (((ra-rb)**2+(yb-ya)**2)**(1/2)-l0)*((yb - ya)/((ra-rb)**2+(yb-ya)**2)**(1/2))

print(kl)
