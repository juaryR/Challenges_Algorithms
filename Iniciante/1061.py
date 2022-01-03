# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

primeiro_dia =  int(input().split()[1])

hora_inicio,min_inicio,seg_inicio =  map(int,input().split(":"))

ultimo_dia =  int(input().split()[1])

hora_fim,min_fim,seg_fim =  map(int,input().split(":"))

# Convert every think in segund 
t1 = primeiro_dia*60*60*24 + hora_inicio*60*60 + min_inicio*60 + seg_inicio

t2 = ultimo_dia*60*60*24 + hora_fim*60*60 + min_fim*60 + seg_fim

# Desconvert every think in segund 

dif = t2 - t1

d  =  dif//(60*60*24)
dif = dif%(60*60*24)

h =  dif//(60*60)
dif = dif%(60*60)

m  =  dif//(60)
dif = dif%(60)


s =  dif

print('{} dia(s)'.format(d))
print('{} hora(s)'.format(h))
print('{} minuto(s)'.format(m))
print('{} segundo(s)'.format(s))
