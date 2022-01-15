# Número Primo

N = int(input())

for i in range(N):
    num = int(input())
    perf = [ J for J in range(1,num+1) if num%J == 0] 
    if len(perf) == 2:
        print('{} eh primo'.format(num))
    else:
        print('{} nao eh primo'.format(num))
    