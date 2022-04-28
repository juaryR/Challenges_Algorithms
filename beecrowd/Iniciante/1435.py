
while True: 
 matriz = input()
 matriz = int(matriz)
 auxiliar = []
 matrizLen = []
 for i in range(matriz):
     for j in range(matriz):
         if(i==j):
             auxiliar.append( 1 )
         else:
             auxiliar.append(abs(i-j)+1)

         matrizLen.append(auxiliar)

 print(matrizLen) 
 if not matriz :
     break 
'''
ordens = []
aux = 1
while(aux != 0):
  aux = int(input())
  if aux != 0:
    ordens.append(aux)

for ordem in ordens:
  matriz = []
  for i in range(ordem):
    auxiliar = []
    for j in range(ordem):
      if(i == j):
        auxiliar.append(1)
      if(i > j):
        auxiliar.append(i - j + 1)
      if(i < j):
        auxiliar.append(j - i + 1)
    matriz.append(auxiliar)

  for i in range(ordem): 
    for j in range(ordem):
      if j == 0:
        print(f"{matriz[i][j]:3d}", end = "") 
      else:
        print(f" {matriz[i][j]:3d}", end = "") 
    print() 
  print()
  '''
