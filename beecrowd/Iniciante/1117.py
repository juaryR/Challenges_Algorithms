from statistics import mean
notas =  []
while True:
    nota =  float(input())
    if nota >= 0 and nota <= 10:
       notas.append(nota)
    else:
        print('nota invalida')
    if len(notas) == 2:
        print('media = {}'.format(mean(notas)))
        break
