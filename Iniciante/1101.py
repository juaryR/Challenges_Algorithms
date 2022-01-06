while True:
    M,N = map(int,input().split())
    if M > N:
        c = M
        M = N
        N = c
    if M <= 0 or  N <= 0:
        break
    
    val= range(M,N+1)
    
    print(" ".join(map(str,val)),"Sum={}".format(sum(val)))