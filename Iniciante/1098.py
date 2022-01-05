I = 0.0
while I <= 2 :
    for J in [1.0,2.0,3.0]:
        A = str(round(J+I,2))
        B = str(round(I,2))
        B = B.rstrip('0').rstrip('.') if '.' in B else B
        A = A.rstrip('0').rstrip('.') if '.' in A else A 
        print("I={} J={}".format(B,A))
    I= I+0.2