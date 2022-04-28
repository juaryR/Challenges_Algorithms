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

# Other solution

#x = int(input())

##Calculo do menor ímpar maior ou igual à x
##  x%2 retorna 1 se x é ímpar
##  (x+1)%2 retorna 1 se x é par
##  se somamos 1 a um x par, ele se torna ímpar
#x += (x+1)%2

# Loop para imprimir os seis valores
#for i in range(6):
#    print(x)
#    x += 2
