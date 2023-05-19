# livinus felix bassey
# 08.3.2017
# Æfingaverkefni_lista



flag=True
while flag:
    print("1. Innkaupalisti")
    print("2. Random tölur")
    print("3. Fyrsta og síðasta")
    print("4. Nemendur")
    print("5. Hætta")
    val=input("Sláðu inn val 1,2,3,4 og 5 til að hætta")
    if val=="1":
        print("þú hefur valið innkaupalista")
    elif val=="2":
         print("þú hefur valið Randomtölur")
    elif val=="3":
         print("þú hefur valið fyrsta og síðasta")
    elif val=="4":
         print("Nemendur")
         nafnalisti=["anna","konni","diddi","villi"]
         x=0
         while x < 3:
             nafn=input("Sláðu inn nafn á nemenda ")
             if nafn in nafnalisti:
                 print("þetta nafn er komið í listann")
                 x=x-1
             else:
                 nafnalisti.append(nafn)
                 print("Nafn hefur verið sett í listann")
             x=x+1
         print(nafnalisti)
         nafnalisti.reverse()
         print(nafnalisti)
    elif val=="5":
        print("bless bless")
        flag=False
    else:
        print("Þú verður að velja 1,2,3,4 eða 5")
