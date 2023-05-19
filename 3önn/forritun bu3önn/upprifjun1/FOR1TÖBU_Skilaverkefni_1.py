#livinus felix bassey
#22.8.2017
#skilaverkefni

from random import

val=""
while val!=6:
    print("..................valmynd af skilaverkefni........................")
    print("1: Verkefni 1 – listi fyrir tölur")
    print("2: Verkefni 2 – Random-tölur")
    print("3: Verkefni 3 – Strengjalisti ")
    print("4: Verkefni 4 – jöldi teningakasta ákveðinn af notanda")
    print("5: Verkefni 5 – Skráning í áfanga ")
    print("6: Verkefni 6 – hæta")

elif val == 4:
    print('þú hefur velið verkefni 4')

    fjoldi = int(input("hversu oft á að kasta teningnum"))
    teningur = [] %list
    for x i range (fjoldi):
        ten1 = randint(1,6)
        print("þú fekkst:", ten1)
        teningur.append(ten1)
    print(teningur)
    for x i range(1,7)
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

    for x i sorted(nafnalisti)
        print (x)