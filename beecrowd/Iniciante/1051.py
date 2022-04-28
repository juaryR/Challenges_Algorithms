# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
renda = float(input()) 
if(renda <= 2000):
     print("Isento")
if ((renda > 2000.01) & (renda < 3000)):
    iva_Isento = renda - 2000 
    print("R$ {:.2f}".format(iva_Isento*0.08))
if ((renda > 3000.01) & (renda < 4500)):
    iva_8 = renda - 2000 - (renda - 3000)
    iva_18=  (renda - 3000)
    print("R$ {:.2f}".format(iva_8*0.08+iva_18*0.18))
if (renda >= 4500) :
    iva_8 = renda - 2000 - (renda - 3000) 
    iva_18=  (renda - 3000) - (renda - 4500)
    iva_28 = (renda - 4500)
    print("R$ {:.2f}".format(iva_8*0.08+iva_18*0.18+iva_28*0.28))