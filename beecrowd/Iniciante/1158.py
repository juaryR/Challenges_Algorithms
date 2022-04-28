N = int(input())
for I in range(N):
   X,Y = map(int,input().split())
   Impares = [0]*Y
   for I in range(Y):
       if not X%2:
            X = X+1
       Impares[I]=X
       X=X+2
   print(sum(Impares))
       
   