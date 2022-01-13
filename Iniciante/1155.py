''' S = 1 + 1/2 + 1/3 + … + 1/100 '''
S = 0
for I in range(1,101):
    S = S + 1/I
print('{:.2f}'.format(S))