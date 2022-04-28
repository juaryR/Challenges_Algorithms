from statistics import mean
numeros = [ float(input()) for i in range(6)]
positivos = [i for i in numeros if i > 0 ] 

print('{} valores positivos'.format(len(positivos)))
print('{:.1f}'.format(mean(positivos)))