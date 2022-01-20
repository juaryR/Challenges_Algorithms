operacao = input()

matriz = []
for i in range(12):
  matriz.append([])
  for j in range(12):
    matriz[-1].append(float(input()))

resultado = 0

for i in range(12):
  for j in range(12):
    if(i < j and i > 12 - j - 1):
      resultado += matriz[i][j]

if operacao == 'M':
  resultado = resultado / 30.0
print(resultado)