N = int(input())

for i in range(N):
    num = int(input())
    perf = [ J for J in range(1,num) if num%J == 0] 
    if sum(perf) == num:
        print('{} eh perfeito'.format(num))
    else:
        print('{} nao eh perfeito'.format(num))
    