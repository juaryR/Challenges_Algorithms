
while True:
  try:
    ordem = int(input())
    matriz = []
    for i in range(ordem):
      auxiliar = []
      for j in range(ordem):
        if(i + j == ordem - 1):
          auxiliar.append(2)
        elif(i == j):
          auxiliar.append(1)
        else:
          auxiliar.append(3)
      matriz.append(auxiliar)
    for i in range(ordem): 
      for j in range(ordem):
        print(matriz[i][j], end = '')
      print() 
  except:
    break