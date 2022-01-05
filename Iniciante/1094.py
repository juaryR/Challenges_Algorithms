Entradas = int(input())
Rato = 0
Sapo = 0
Coelho = 0
Total = 0
for i in range(Entradas):
    cobaia,Tipo = input().split()
    if Tipo == 'C':
        Coelho += int(cobaia)
    if Tipo == 'S':
        Sapo += int(cobaia)
    if Tipo == 'R':
        Rato += int(cobaia)
    Total += int(cobaia)
print('Total: {} cobaias'.format(Total))
print('Total de coelhos: {}'.format(Coelho))
print('Total de ratos: {}'.format(Rato))
print('Total de sapos: {}'.format(Sapo))
print('Percentual de coelhos: {:.2f} %'.format((Coelho/Total)*100.00))
print('Percentual de ratos: {:.2f} %'.format((Rato/Total)*100.00))
print('Percentual de sapos: {:.2f} %'.format((Sapo/Total)*100.00))