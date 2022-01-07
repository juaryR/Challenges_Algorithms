from statistics import mean
notas =  []
novo_calc = ''
while True:
    nota =  float(input())
    if nota >= 0 and nota <= 10:
       notas.append(nota)
    else:
        print('nota invalida')
    if len(notas) == 2:
        print('media = {:.2f}'.format(mean(notas)))
        while True:
            if novo_calc == '2':
                exit()
            novo_calc = input("novo calculo (1-sim 2-nao)\n")
            if novo_calc == '1':
                notas =  []
                break
