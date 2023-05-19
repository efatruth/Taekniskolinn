#livinus felix bassey
#22.8.2017
#skilaverkefni

from random import*

val=0
while val!=6:
    print("..................valmynd af skilaverkefni........................")
    print("1: Verkefni 1 – listi fyrir tölur")
    print("2: Verkefni 2 – Random-tölur")
    print("3: Verkefni 3 – Strengjalisti ")
    print("4: Verkefni 4 – jöldi teningakasta ákveðinn af notanda")
    print("5: Verkefni 5 – Skráning í áfanga ")
    print("6: Verkefni 6 – hæta")
    val=int(input("veldu dæmi - 1,2,3,4,5 eða 0 til að hætta"))


    if val==1:
        print('þú hefur velið verkefni 1')
        teljari=0
        listi2=[]
        talnalist=[]
        #innsláttur
        for x in range(7):
            tala = int(input("sláðu inn tölu"))
            talnalisti.append(tala)
        #raðaður listinn
        talnalist.sort()#raða listanum
        print(talnalist)
        print("heðsta talan er =",max(talnalist))
        print("lagsta talan er =", min(talnalist))
        print("summa talan er =", sum(talnalist))
        print("meðaltal talnana er =", round(sum(talnalist) / len(talnalisti),2))
        #for slaufa fyrir display
        for x in talnalist:
            print(x, end=";")
            if x <=50.5:
                teljari += 1
                listi2.append(x)
        print("\nþessar tölur eru fyrir neðan 50,5")
        for x in listi2:
            print(x, end=",")
        print("\nþað eru ",teljari,"tölu sem eru minni en 50,5°")


    elif val == 2:
        print('þú hefur velið verkefni 2\n')
        telja_up = 0
        telja_down = 0
        temptala = 0
        ranlist = [] #þetta er listi fyrir tölur
        for x in range(70):#þetta keyrir 70 sinum
            temptala = randint(1,501)
            ranlist.append(temptala)#þetta er set in lista og kallar eftir random tölu frá 1 up í 500
            if temptala < 251:
                telja_down += 1
            else:
                telja_up += 1
        #þetta þarf aðra forlykkju ekki range til að birta tölunnar
        for i in range(len(ranlist)):
            if i % 4 !=3:
                print(ranlist[i], end="\t")
            else:
                print(ranlist[i])
        print("")

        print("\nstærsta talan er =", max(ranlist))
        print("\minnsta talan er =", max(ranlist), "\n")
        #herna notum reverse
        ranlist.reverse()
        for x in range(len(ranlist)):
            if x % 6 != 5:
                print(ranlist[x], end="\t")
            else:
                print(ranlist[x])
        print("")

        print("\nfjöldi talna undir 251 er", telja_down)
        print("\fjöldi talna yfir 250 er", telja_up)




    elif val == 3:
        print('þú hefur velið verkefni 3\n')
        nafnlisti = []
        #innsláttur
        print('sláðu inn 5 nöfn fyrir neðan')
        for x in range(5):
            nafn = input("")
            nafnlisti.append(nafn)

        #herna er valmynd önnur
        val2=""
        while val2!="5":    # herna hadu afram þanngað til val2 verður 5
            print("\n................................")
            print("1	Birta nöfnin óraðað.")
            print("2	Raða nöfnunum í stafrófsröð og birta.")
            print("3	Raða nöfnunum í öfuga stafrófsröð og birta.")
            print("4	Birta eitt nafn eftir því hvaða númer 1-5 var valið.")
            print("5	Hætta í verkefni 3.")
            print("................................")
            val2 = input("veldu lið")

            if val2 == "1":
                for x in nafnalisti:
                    print(x)

            elif val2 == "2":
                nafnalisti.sort()
                print(nafnalisti)

            elif val2 == "3":
                nafnalisti.reverse()
                print(nafnalisti)

            elif val2 == "3":
                valnafn = int(input("veldu numer á nafninu"))
                print(nafnalisti[valnafn - 1])
            elif val2 =="4":
                syna_nafn = int(input("hvað er númer? "))
                print("nafnið er", nafnalisti[syna_nafn-1])
            elif val2 == "5":
                print("þákk fyrir")
            else:
                print("upps eithvað")


    elif val == 4:
        print('þú hefur velið verkefni 4')

        fjoldi = int(input("hversu oft á að kasta teningnum"))
        teningur = [] # list
        for x in range (fjoldi):
            ten1 = randint(1,6)
            print("þú fekkst:", ten1)
            teningur.append(ten1)
        print(teningur)
        for x in range(1,7):
            print("fjoldi", x, ";", teningur.count(x))
        hlid.append(teningur.count(x))

        print(hlid.index(min(hlid))+1, "kom sjalnast upp ")
        print(hlid.index(max(hlid))+1, "kom oftast upp ")


    elif val == 5:
        print('þú hefur velið verkefni 5')
        fjoldi = int(input("hversu margir eru skráðir í hópinn"))
        nafnalista = []
        print("skrifaðu nöfnin fyrir neðan ")
        for x in range(fjoldi):
            nafn = input("")
            nafnalista.append(nafn)

        for x in sorted(nafnalista):
            print (x)

    elif val == 6:
        print("þákk fyrir")
    else:
        print("upps eithvað")