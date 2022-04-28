while True:
    x,y = map(int,input().split())
    ''' 1Q '''
    if x>0 and y > 0:
        print('primeiro')
    ''' 2Q '''
    if x < 0 and y > 0:
        print('segundo')
    ''' 3Q '''
    if x < 0 and y < 0:
        print('terceiro')
    ''' 4Q '''
    if x > 0 and y < 0:
        print('quarto')
    if x == 0 or y == 0:
        break