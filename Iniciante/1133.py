X = int(input())
Y = int(input())
if X > Y:
    c = X
    X = Y 
    Y = c 

print("\n".join(map(str,[ i for i in range(X+1,Y) if  i%5 == 2 or i%5 == 3  ])))
