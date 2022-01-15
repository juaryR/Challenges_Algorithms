while True:
   
   X = int(input())
   if X == 0:
       break
   Y = 5 
   pares = [0]*Y
   for I in range(Y):
       if X%2:
            X = X+1
       pares[I]=X
       X=X+2
   print(sum(pares))
   