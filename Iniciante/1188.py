
Entrada = input()
m = []
for _ in range(12):
    m.append([])
    for _ in range(12):
        v = float(input())
        m[-1].append(v)

k = 0
soma = 0
for i in range(12):
    for j in range(12):
        if (11 - i) < j < i:
            k += 1
            soma += m[i][j] 

if Entrada == 'M':
    resultado = soma/k
elif Entrada == 'S':
    resultado = soma

print('{:.1f}'.format(resultado))