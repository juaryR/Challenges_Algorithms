from statistics import mean
media = []
while True:
    num = int(input())
    if num < 0:
        break
    media.append(num)
print('{:.2f}'.format(mean(media)))