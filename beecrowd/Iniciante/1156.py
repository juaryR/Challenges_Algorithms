'''  S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/? '''
num  = [ I for I in range(1,40,2)  ]
dem  = [ 2**J for J in range(1,len(num))]
dem.insert(0,1)
frac = [b/m for b,m in zip(num,dem)]
print('{:.2f}'.format(sum(frac)))