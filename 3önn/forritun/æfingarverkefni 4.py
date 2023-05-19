#Livinus felix bassey
#01.03.2017
# æfingarverkefni 4: skoðum forlykkjur , lykkjur sem endurtaka kóða ákveðid oft

#liður 1

for i in range(5): 
    print (i)   # prentar út 0 til 4
for i in range(5): 
    print (i + 1) # prentar út 1 til 5
    
print('----')
    
'''for i in range(5):
    i = i + 1
    print (i)
for i in range(5):
    print (i)'''

for i in range(5, 12):
    print (i)       # prentar út 5 til 11
for i in range(5, 12):
    print (i+1)     # prentar út 6 til 12
    
print('----')
    

for i in range(5, 15, 3):
    print (i)       # prentar út 5 - 8 - 11 - 14

print('----')
# til er fyrirbærið listi sem er safn af breytum, skoðum þá síðar
# forlykkjur geta farið stak fyrir stak 1 gegnum slíka lista
listi_nofn = ['Eyþór', 'Alice', 'Snorri', 'dav', 'konni'] # svona litur listi
# notum forlykkjur til að fara í gegnum listann stak fyrir stak
for stak in listi_nofn:
    print(stak, end=' - ') #skoðum end betur seinna, fer ekki nýja linu
print('þetta var nú aldeilis gaman')
