def impar(dados):
    Result = 0
    X,Y = map(int,dados)
    if X > Y:
        c = X
        X = Y
        Y = c
    if X ==Y:
        return 0 
    for i in range(X+1,Y):
        if i%2:
            Result = Result+i
    return Result


N = int(input())
dados = [input().split()for i in range(N)]
for i in dados:   
    print(impar(i))