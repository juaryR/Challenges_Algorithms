Entradas = int(input())

dados = [ int(input()) for i in range(Entradas)]

def checkOddEven(valr):
    if valr > 0:
       return "EVEN POSITIVE" if valr % 2 == 0 else "ODD POSITIVE"
    if valr < 0:
       return "EVEN NEGATIVE" if valr % 2 == 0 else "ODD NEGATIVE"
    if valr == 0:
        return "NULL"
         
for a in list(map(checkOddEven,dados)):
    print(a)
