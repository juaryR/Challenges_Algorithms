empates = 0
pont_G = 0
pont_I = 0
sair = ''
while sair !='2':
       inter,gremio = map(int,input().split())
       if inter > gremio:
           pont_I =pont_I+ 1 
       else:
           pont_G =pont_G + 1  
       if inter == gremio:
           empates += 1
       sair =  input("Novo grenal (1-sim 2-nao)\n")

print('{} grenais'.format(pont_I+pont_G+empates))
print('Inter:{}'.format(pont_I))
print('Gremio:{}'.format(pont_G))
print('Empates:{}'.format(empates))
print ("{} venceu mais".format("Inter" if   pont_I > pont_G else "Gremio"))