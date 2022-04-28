X = [ int(input()) for I in range(10)]
for J,I in enumerate(X):
    if I <= 0:
        I = 1
    print('X[{}] = {}'.format(J,I))
