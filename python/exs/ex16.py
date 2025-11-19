#digitar numero com virgula e ele tira ela com import trunc
from math import trunc
num = float(input("Digite um número com virgula: "))
print(f'numero arredondado {trunc(num)}' )

#agora com int
num = float(input('digite outro numero com virgula'))
print(f'aqui seu numero sem virgula {int(num)}')


