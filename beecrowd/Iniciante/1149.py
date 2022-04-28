valores = map(int,input().split())
valr = []
for i in valores:
    if i > 0:
        valr.append(i)
    if len(valr) == 2:
        break
A,N = valr
result = 0
for i in range(N):
    result += A + i

print(result)