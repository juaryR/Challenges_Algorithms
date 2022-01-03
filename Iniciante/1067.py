num = int(input())


# Impares 
impares = [i for i in range(num+1) if i % 2 ] 

for impar in impares:
    print('{}'.format(impar))