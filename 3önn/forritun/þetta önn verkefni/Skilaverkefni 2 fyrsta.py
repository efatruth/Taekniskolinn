# Livinus Felix Bassey
# 18.1.2017
# Skilaverkefni 2

#Liður 1
#hérna er um þrjár heiltölur.
print("ekki sláðu sömu tölu tvísvar")
tala1 = int(input("Hver er fyrsta talan "))
tala2 = int(input("Hver er önnur talan "))
tala3 = int(input("Hver er sú þriðja "))

if tala1 == tala2 or tala1 == tala3 or tala2 == tala3:
    print("þarna gerðiru mistök")
else:
     if tala1 > tala2 and tala1 > tala3:
         print("tala1 er stærst")
     elif tala2 > tala1 and tala2 > tala3:
         print("tala2 er stærst")
     else: print("tala3 er stærst")
     


#Liður 2
#hérna er sentimetra eða öfugt.
svar = input("viltur breyta tommum í sentimetra(t)/(s) ").lower()
utkoma = 0.0
utkoma2 = 0.0
tommur = 0.0
sentimetrar = 0.0
if svar == "t":
#setur hérna inn hversu margar tommur eiga að breytast í sentimetra
    tommur = float(input("sláðu inn hversu margar tommunar eru "))
    utkoma = tommur * 2.54
print("þetta eru", utkoma, "sentimetrar")
if svar == "s":
# hérna ef hann vill breyta sentimetrum í tommur
    sentimetrar =int(input("Hversu margir sentimetrar "))
    utkoma2 = sentimetrar / 2.54
print("þetta verða ", format(utkoma2, ".2f"), "tommur")



#Liður 3
#Hérna nalast árstíðirnar eftir tölum frá 1 - 12 ef notandi slær inn aðra tölu kemur fram RANGUR INNSLÁTTUR
arstidir = int(input("Hvaða mánuður er settu inn tölu frá 1 - 12"))

#tala 1 - 3
if arstidir >=1 and arstidir <=3:
    print("Nú er daginn tekið að lengja")
#tala 4 - 5
elif arstidir >=4 and arstidir <=5:
    print("Vorið er komið og grundirnar gróa")

#tala 6 - 8    
elif arstidir >=6 and arstidir <=8:
    print("Núnar er sumarið komið með blóm í haga")
    
#tala 9 - 10
elif arstidir >=9 and arstidir <=10:
    print("Núnar er haustið gengið í garð")
    
#tala 11 - 12
elif arstidir >=11 and arstidir <=12:
    print("Núnar styttist í jólinn")
else:
    print("RANGUR INNSLÁTTUR")



#Liður 4
#Hérna setur inn nafn kyn og 2 heiltölur    
nafn = input("Hvað heitirðu")
kyn = input("Hvers kyns ertu")
tala4 = int(input("Veldu tölu"))
tala5 = int(input("Veldu aðra tölu"))
#hérna skrifa ég upp hvor er stærri eða hvort tölurnar seú jafnstórar
if tala4 > tala5:
    print("tala1 er stærri")
elif tala5 > tala4:
    print("tala2 er stærri")
elif tala4 == tala5:
    print("þær eru jafnstórar")
#og skrái síðan eftir kyni blessuð/aður ásamt nafni nema notandi hafi sett inn rangan innslátt
if kyn == 'kk':
    print("blessaður", nafn)
elif kyn == 'kvk':
    print("blessuð", nafn)
else:
    print("blessaður eða blessuð veit ekki hvors kyns þú ert")



#Liður 5
#slá inn tölu lægri en 0 og hærri en 10 annars færðu svarið ef þú slærð þar inn
tala6 = int(input("Sláðu inn tölu"))
if tala6 == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
    print("þessi tala er ekki lægri en núll eða hærri en 10")
else:
    print("vel gert")
    
    
    
