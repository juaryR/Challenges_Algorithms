'''Ultrapassando Z'''
X = int(input())
while True:
    Z = int(input())
    if Z > X:
        a = [X] 
        for i in range(X,Z):
            if sum(a) > Z : 
                break
            a.append(i)
        print(len(a))
        break
