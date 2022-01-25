from statistics import mean 
ordem = int(input())

operador = input() # S - soma ;  M - Media 

matriz = [] # M[12][12]
linha = []

for i in range(12):
    linha =  [input() for _ in range(12)]
    matriz.append(linha)

if operador == "S":
    if ordem <= 11 and ordem >= 0:
        print("{:.1f}".format(sum(map(float,matriz[ordem]))))

    

if operador == "M":
    if ordem <= 11 and ordem >= 0:
        print("{:.1f}".format(mean(map(float,matriz[ordem]))))