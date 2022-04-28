from statistics import mean


def media_pond(vetor):
    vetor = list(vetor)
    if len(vetor) == 3:
        return float((vetor[0]*2 + vetor[1]*3 + vetor[2]*5)/(2+3+5))
    else:
        return mean(vetor)

num = int(input())
casos = [map(float,input().split()) for i in range(1,num+1) ]

result = list(map(media_pond,casos))
for i in result:
    print("{:.1f}".format(i))