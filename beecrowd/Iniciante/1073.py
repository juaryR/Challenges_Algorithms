'''Quadrado de Pares'''
''' N (5 < N < 2000).'''
num = int(input())

pares = [ (i,i**2) for i in range(1,num+1) if not i % 2]

for par in pares:
    print('{}^2 = {}'.format(par[0],par[1]))
