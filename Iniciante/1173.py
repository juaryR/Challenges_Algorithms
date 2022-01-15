X = int(input())
A = [X]*10
print('N[{}] = {}'.format(0,X))
for i in range(1,10):
    A[i] = X*2
    X = A[i]
    print('N[{}] = {}'.format(i,X))