# livinus felix bassey
# 08.3.2017
# Æfingaverkefni_07_For-lykkjur

#liður A: Talnabil
#hérna er forrit sem prentar allar tölur á ákveðnu bili, frá 10 upp í 100.
for x in range(10,101):
    print(x)
    
#liður B: Innslegið_Talnabil
#þetta er forrit sem les inn tvær heiltölur frá lyklaborði og prentar út á skjáinn allar
#tölur á bilinu á milli talnanna.
tala1=int(input("Sláðu inn tölu  eitt"))
tala2=int(input("Sláðu inn tölu tvö .Hún m+a ekki vera lægri en tala eitt"))
if tala1==tala2:
          print("Þessar tölur eru jafnar")
elif (tala1+1)==tala2:# ef talan er einum hærri
          print ("það eru engar tölur á milli þessara talna")
else:
          for x in range(tala1,tala2+1):
              print(x)

#liður C: Talnabil_UppNidur
#hérna er forrit sem skrifar út allar tölur á ákveðnu bili frá byrjunartölu að lokatölu.
tala11=int(input("Sláðu inn tölu  eitt"))
tala22=int(input("Sláðu inn tölu tvö .ekki sama tala og tala eitt"))
if tala11 < tala22:
    for x in range(tala11,tala22+1):
        print(x)
else:
    for x in range(tala11,(tala22-1),-1):#byrjar á hærri tölunni og endar á lægri steppar niður
        print(x)

#liður D: Oddatolur
#hérna er forrit sem skrifar út allar oddatölur á ákveðnu bili.
tala11=int(input("Sláðu inn tölu  eitt"))
tala22=int(input("Sláðu inn tölu tvö .ekki sama tala og tala eitt"))
if tala11 < tala22:
    for x in range(tala11,tala22+1):
        if x % 2==1:#allar oddatölur
            print(x)
else:
    for x in range(tala11,(tala22-1),-1):#byrjar á hærri tölunni og endar á lægri steppar niður
        if x % 2==1:#allar oddatölur
            print(x)

#liður E: Annað veldi
#hér forrit prentar allar tölur á ákveðnu bili.
tala111=int(input("Sláðu inn tölu  eitt"))
tala222=int(input("Sláðu inn tölu tvö .ekki sama tala og tala eitt"))
for x in range(tala111,tala222+1):
    print(x," ",(x*x))

#liður F: Summa
#forrit leggur saman allar tölur á ákveðnu bili. 
tala3=int(input("Sláðu inn tölu  eitt"))
tala4=int(input("Sláðu inn tölu tvö .ekki sama tala og tala eitt"))
summa=0
for x in range(tala3,tala4+1):
    summa=summa+x
    if x < tala4:
        print(x,end="+")#skiptir ekki um línu
    else:
        print(x,end="")#þetta á að gera í síðast skiptið
print("=",summa)

#liður G: Margföldunartafla
#hér forrit skrifar út  margföldunartöflu.
tafla=0
magfold=int(input("Hvaða margföldunartöflu viltu að ég birti??"))
if magfold<=10:
    tafla=10
else:
    tafla=magfold
for x in range(tafla+1):#keyrir 10 sinnum
    print(x,"*",magfold,"=",(magfold*x))
    
    
'''
#liður H
#BMI eða Body Mass Index er skilgreindur á eftirfarandi hátt.
#BMI = þyngd í kg / (hæð í metrum)2
#Búið til forrit sem spyr um hæð í metrum en forritið sýnir BMI fyrir þessa hæð, en fyrir
#þyngdir á milli 60 og 125 kg. þar sem hlaupið er á 5 kg. bilum.
haed=float(input("Sláðu inn hæð í metrum"))
print("BMI fyrir þessa hæð er:")
print("Þyngd        BMI")
BMI=0
for x in range(60,126,5):#hleypur á 5kg bili
    BMI=x/(haed*haed)
   
    if x<100:
         print(x,"   ",format(BMI,".2f"))
    else:
        print(x,"  ",format(BMI,".2f"))'''























        
