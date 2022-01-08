X = int(input())
Y = int(input())
if X > Y:
    c = X
    X = Y 
    Y = c 

print(sum([ i for i in range(X,Y+1) if  i%13  ]) if X != Y else 0)
