X = [float(input()) for i in range(100)]
for I,J in enumerate(X):
    if J <= 10:
        print('A[{}] = {:.1f}'.format(I,J))