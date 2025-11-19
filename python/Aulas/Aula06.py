#Tipos primitivos

#int = inteiro
#flooat = numero com '.' (ex. 2.4)
#bool = Boleano / true ou False
#str = palavra

n1 = int(input('Digite um número:'))
n2 = int(input('digite mais um número:'))
s = n1 + n2
print('01. A soma vale',s)
print('02. A soma vale {}'.format(s))
print(f'04. A soma de {n1} e {n2} é {s}')
print('05. A soma de {} e {} é {}'.format(n1 ,n2 ,s))