## Primeira solução 
#i = 0
#a = []
#positivos = 0 

#a.append(input())  
#a.append(input())  
#a.append(input())  
#a.append(input())  
#a.append(input())
#a.append(input())    

#for num in a:
#    if num.isnumeric():
#        if int(num) > 0 :
#            positivos = positivos+1 


## Outra solução 


nums = [float(input()) for i in range(6)]
positivos = len([ i for i in nums if i > 0])

print(f'{positivos} valores positivos')