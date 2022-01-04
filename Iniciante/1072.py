Entradas = int(input())

dados = [ int(input()) for i in range(Entradas)]
intervalo = [10,20] 
dentro  = [ i for i in dados if i > 10 & i < 20 ]
fora = len(dados)-len(dentro)
print("{} in".format(len(dentro)))
print("{} out".format(fora))