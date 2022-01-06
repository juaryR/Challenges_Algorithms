while True:
    M,N = map(int,input().split())
    if M > N:
       print('Decrescente')
    if M == N:
        break
    if M <  N:
       print('Crescente')
