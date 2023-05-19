#Livinus felix bassey
#01.03.2017



#Búið til forrit sem prentar allar tölur á ákveðnu bili, t.d. frá 10 upp í 100.
#Þið ákveðið bilið sem er valið.
for x in range(10,101):
    print(x)
#liður 2
#Skrifið forrit sem les inn tvær heiltölur frá lyklaborði og prentar út á skjáinn allar
#tölur á bilinu á milli talnanna. Prentið út á skjáinn villuskilaboð ef engar tölur
#finnast á bilinu þ.e. tölurnar eru jafn háar eða önnur aðeins einum hærri en hin.
tala1=int(input("Sláðu inn tölu  eitt"))
tala2=int(input("Sláðu inn tölu tvö .Hún m+a ekki vera lægri en tala eitt"))
if tala1==tala2:
          print("Þessar tölur eru jafnar")
elif (tala1+1)==tala2:# ef talan er einum hærri
          print ("það eru engar tölur á milli þessara talna")
else:
          for x in range(tala1,tala2+1):
              print(x)

#liður 3
#Búið til forrit sem skrifar út allar tölur á ákveðnu bili frá byrjunartölu að lokatölu. 
#T.d. ef bilið er frá 6 upp í 11 eiga að skrifast út tölurnar 6 7 8 9 10 11 í þessari
#Röð.  Ef valið er bilið frá 11 til 6 á að skrifast 11 10 9 8 7 6 í þessari röð.
#Notandinn á að ákveða hvaða bil er valið.
tala11=int(input("Sláðu inn tölu  eitt"))
tala22=int(input("Sláðu inn tölu tvö .ekki sama tala og tala eitt"))
if tala11 < tala22:
    for x in range(tala11,tala22+1):
        print(x)
else:
    for x in range(tala11,(tala22-1),-1):#byrjar á hærri tölunni og endar á lægri steppar niður
        print(x)

#liður 4
#(Oddatolur) Búið til forrit sem skrifar út allar oddatölur á ákveðnu bili. T.d. ef
#bilið er frá 6 upp í 11 eiga að skrifast út tölurnar 7 9 og 11. Sama myndi skrifast
#út ef valið er bilið frá 7 upp í 12.  Notandinn á að ákveða hvaða bil er valið.
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

#liður 5 annað veldi
#Búið til forrit sem prentar allar tölur á ákveðnu bili
#og hvað talan er í öðru veldi.
#Til dæmis ef bilið er frá 2 upp í 4 þá skrifast út:
tala111=int(input("Sláðu inn tölu  eitt"))
tala222=int(input("Sláðu inn tölu tvö .ekki sama tala og tala eitt"))
for x in range(tala111,tala222+1):
    print(x," ",(x*x))

#liður 6 
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

#Búið til forrit sem skrifar út  margföldunartöflu.
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






















        
