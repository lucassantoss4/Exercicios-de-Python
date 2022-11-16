import math
import random

n1 = random.randint(1 , 10)
n2= random.randint(1, 10)
c1 = n1 ** 2
c2 = n2 ** 2
print(f'Com os catetos {n1} e {n2} sendo elevados ao quadrado, a hipotenusa é igua a {(c1+c2) ** (1/2):.2f}')