from statistics import mean 
ordem = int(input())

operador = input() # S - soma ;  M - Media 

matriz = [] # M[12][12]
linha = []
coluna = []
for i in range(2):
    linha =  [input() for _ in range(2)]
    matriz.append(linha)

for linha in matriz:
    coluna.append(linha[ordem])

if operador == "S":
    if ordem <= 11 and ordem >= 0:
        print("{:.1f}".format(sum(map(float,coluna))))

    

if operador == "M":
    if ordem <= 11 and ordem >= 0:
        print("{:.1f}".format(mean(map(float,coluna))))