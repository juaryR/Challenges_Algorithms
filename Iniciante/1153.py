'''Fatorial Simples'''

'''N = N * (N-1) * (N-2) * (N-3) * ... * 1.'''
N = int(input())
fact = 1
for i in range(N,0,-1):
    fact = fact*i

print(fact)