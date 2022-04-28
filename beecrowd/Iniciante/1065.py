numeros = [ float(input()) for i in range(5)]
par = [i for i in numeros if not i % 2 ] 

print('{} valores pares'.format(len(par)))