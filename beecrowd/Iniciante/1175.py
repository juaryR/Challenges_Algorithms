X = [int(input()) for i in range(20)]
X.reverse()
for I,J in enumerate(X):
    print('N[{}] = {}'.format(I,J))