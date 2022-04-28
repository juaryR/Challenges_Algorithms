#num = int(input())

#pares = [ (i,i*num) for i in range(1,11)]

#for par in pares:
#    print('{} x {} = {}'.format(par[0],num,par[1]))

## Opção otimizada 

num = int(input())

for multiplicador in range(1, 11):
    print(f'{multiplicador} x {num} = {multiplicador * num}')