casos = [int(input()) for i in range(100)]
maior = max(casos)
pos = casos.index(maior) 

print(maior)
print(pos+1)