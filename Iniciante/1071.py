X = int(input())
Y = int(input())

if Y < X:
    c = X
    X = Y 
    Y = c

impares = [i for i in range(X+1,Y) if i % 2 ] 

print(sum(impares))