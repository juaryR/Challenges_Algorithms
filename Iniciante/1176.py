cases = int(input())
for  i in range(cases):
    n = int(input())
    V1 = [0 for i in range(n+1) ]
    for i in range (0,n+1):
        if i <= 1:
            V1[i] = i
        else:
            V1[i] = V1[i-1] + V1[i-2]
    print('Fib({}) = {}'.format(n,V1[n]))
