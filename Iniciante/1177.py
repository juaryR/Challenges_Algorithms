N = int(input())
contador = 0
for I in range(10):
    print('N[{}] = {}'.format(I,contador))
    if contador < N-1 :
        contador = contador+1
    else:
        contador=0