#calcular hipotenusa

import math
from math import sqrt

ca = float(input('tamanho de um catetp:'))
co = float(input('tamanho do outro cateto: '))
h1 = ca ** 2 + co ** 2
h2 = math.sqrt(h1)
print(f'a hipotnuza dos catetos {ca} e {co} é {h2 :.2f}')

print('-----------de outro jeito--------------------------------------------------------------------')

ca = float(input('tamanho de um cateto:'))
co = float(input('tamanho do outro cateto: '))
h1 = math.hypot(ca, co)
print(f'a hipotenuza de {ca} e {co} é {h1 :.2f}')

print('-----------de outro jeito--------------------------------------------------------------------')

co = float(input('cateto 1 '))
ca = float(input('cateto 2 '))
h1 = (co ** 2 + ca ** 2) ** (1/2)
print(f'a hipotenuza de {co} e {ca} é {h1 :.2f}')

