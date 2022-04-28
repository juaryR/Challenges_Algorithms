n = int(input())
# WORK but have Time limit exceeded
# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))


# fibo =  [ recur_fibo(i) for i in range(n)]

# print(' '.join(map(str,fibo)).strip())


V1 = [0 for i in range(n)]
for i in range (0,n):
    if i <= 1:
        V1[i] = i
    else:
        V1[i] = V1[i-1] + V1[i-2]

    if i==n-1:
        print('%d'%(V1[i]),end='')
    else:
        print('%d'%(V1[i]),end=' ')
    
print()