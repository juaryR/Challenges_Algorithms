while True:
    val = int(input())
    if val == 0:
        break
    print((" ".join(map(str,range(1,val+1)))).strip())