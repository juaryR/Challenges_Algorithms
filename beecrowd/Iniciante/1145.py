x,y = map(int,input().split())
val = [i  for i in  range(1,1+y)]
a = ''
for i in val:
    a += str(i) + ' '
    if not i%x:
        print( a.strip())
        a = ''