
numeros = [ float(input()) for i in range(5)]

# Pares 
par = [i for i in numeros if not i % 2 ] 
# Impares 
impar = [i for i in numeros if i % 2 ] 
# Positivos 
positivos = [i for i in numeros if i > 0 ] 
# Negativos 
negativos = [i for i in numeros if i < 0 ] 

print('{} valor(es) par(es)'.format(len(par)))
print('{} valor(es) impar(es)'.format(len(impar)))
print('{} valor(es) positivo(s)'.format(len(positivos)))
print('{} valor(es) negativo(s)'.format(len(negativos)))