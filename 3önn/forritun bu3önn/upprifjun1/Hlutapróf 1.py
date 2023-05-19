#livinus felix bassey
#19.09.2017
#Hlutapróf 1

from random import*

val = 0
while val!=4:
    print("..................valmynd........................")
    print("1: Listir")
    print("2: Strengur")
    print("3: Föll ")
    print("4: Hætta")
    val = int(input("hvaða lið veluðu"))

    if val == 1:
        print('þú hefur velið listi')
        telja_up = 0
        telja_down = 0
        temptala = 0
        ranlist = [] #þetta er listi fyrir tölur
        for x in range(20):#þetta keyrir 20 sinum
            temptala = randint(10,21)
            ranlist.append(temptala)#þetta er set in lista og kallar eftir random tölu frá 1 up í 21
        for tala in ranlist:
            print(tala, end="-")
        print()
        for tala in ranlist:
            if tala == 15:
                ranlist.remove(tala)
        print(ranlist)

        for i in range(len(ranlist)):
            if ranlist[i] == 20:
                ranlist[i] = 25
        print(ranlist)

        medaltal = sum(ranlist)/len(ranlist)
        print(medaltal)


    elif val == 2:
        print('þú hefur velið strengur')
        orð = input("veldu þer orð ")
        orð = (len(orð))
        print("það eru ", orð, "stafir í textanum")

        print("skrifar 2 orð og forritið finnur svo hvert er lengst")
        nafn1 = input("segðu eitt orð ")
        nafn2 = input("segðu annað orð")

        for X in range(len(nafn1)):
            print(X)
        print(nafn1, ':', len(nafn1))
        for Y in range(len(nafn2)):
            print(Y)
        print(nafn2, ':', len(nafn2))

        if (len(nafn1)) > (len(nafn2)):
            print("þetta ord er lengra", nafn1)
        elif (len(nafn1)) < (len(nafn2)):
            print("þetta ord er lengra", nafn2)

        strengum = input("settu inn strengum")
        print("hérna er það bæði fram og áfturábak", strengum, strengum[::-1])


    elif val == 3:
        print('þú hefur velið föll')
        def reikna_ágodi(soluverd):
            agodi = 0
            for item in soluverd:
                agodi=(söluverð -(innkaupsverð+ virðsaukaskatt))
            return agodi
        innkaupsverð = [2000, 3000, 5000]
        virðsaukaskatt = [1000, 2000, 3000]

        innkaup_sverð=reikna_agodi(innkaupsverð)
        virðsauka_skatt=reikna_agodi(virðsaukaskatt)

        print('innkaupsverð það er:',innkaup_sverð)
        print('virðsaukaskatt það er:', virðsauka_skatt)


