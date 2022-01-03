import itertools

num = int(input())


# Impares 
impares = []
for i in  itertools.count(start=num):
    if i % 2:
        impares.append(i)
    if len(impares) > 5:
        break 

for impar in impares:
    print('{}'.format(impar))

