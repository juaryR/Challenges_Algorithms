N = int(input())
vetor_x = list(map(int,input().split()))
if  len(vetor_x) == N:
    print('Menor valor: {}'.format(min(vetor_x)))
    print('Posicao: {}'.format(vetor_x.index(min(vetor_x))))