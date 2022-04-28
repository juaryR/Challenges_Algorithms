# pares 
pares = []
# impares 
impares  = []

for i in range(15):
    entrada = int(input())
    if not entrada%2:
        pares.append(entrada)
    else:
        impares.append(entrada)
       
    if len(pares) == 5:
            for key,val in enumerate(pares):
                print('par[{}] = {}'.format(key,val))
            pares = []
    if len(impares) == 5:
            for key,val in enumerate(impares):
                print('impar[{}] = {}'.format(key,val))
            impares = []
if len(impares):
    for key,val in enumerate(impares):
        print('impar[{}] = {}'.format(key,val))
if len(pares):
    for key,val in enumerate(pares):
        print('par[{}] = {}'.format(key,val))
