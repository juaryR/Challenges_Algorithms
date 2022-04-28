'''1.Álcool 2.Gasolina 3.Diesel 4.Fim'''
alcool = 0
Diesel = 0
Gasolina = 0
case = ''

while case != "4":
    case = input()
    if case =="1":
        alcool += 1
    if case =="2":
        Gasolina += 1
    if case =="3":
        Diesel += 1

print('MUITO OBRIGADO')
print('Alcool: {}'.format(alcool))
print('Gasolina: {}'.format(Gasolina))
print('Diesel: {}'.format(Diesel))
      