from statistics import mean
operador = input()

linha = []
valor = 12
soma_media = []
total = 0
diag = []
for i in range(valor):
    for j in range(valor):
        if j > i:
            linha.append(input())
        else:
            _ = input()
            
    diag = diag + linha
    linha=[]

if operador == 'S':
        total =  sum(map(float,diag))
if operador == 'M':
        total = mean(map(float,diag))
    
print("{:.1f}".format(total))


