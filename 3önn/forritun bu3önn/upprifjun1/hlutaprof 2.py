'''
livinus felix bassey
hlutaprof 2
12.10.17
'''
litum_tuple = ('GULUR','APPELSÍNUGULUR','RAUÐUR','GRÆNN','BLÁR','FJÓLUBLÁR')
for x in range(len(litum_tuple)):
    print('Litur', x+1, 'er', litum_tuple[x])# útskrift af litini
    
for lit in litum_tuple:
    if len(lit) >=6:
        print(lit)
lita_listi = ()
for tumlist in range(len(litum_tuple)):
    for tum in range(tumlist+1,len(litum_tuple)+1 ):
        lita_listi.append(litum_tuple[lita_listi] )
print(tumlist)

import random
rand_dict = {1:'GULUR',2:'APPELSÍNUGULUR',3:'RAUÐUR',4:'GRÆNN',5:'BLÁR',6:'FJÓLUBLÁR'}
for i in range(21):
   tala = random.randrange(1,21)
   print(tala)
   

bokheil = {'G':1,'A':2,'R':3,'B':4,'C':5,'F':6}

tuple_a=('11','14','15','16','17','18','19')
nafn = input('Hað er nafn þinn')
if nafn in nafn:
     print('nafn',tuple_a)

   
