# livinus felix bassey
# 06.4.2017
# skilaverkefni6 - lista

import random
aftur = "já"
val = 0
while val != 5:
    print("1. random tolur")
    print("2. talnabil")
    print("3. strengjalista")
    print("4. samaqnbuður")
    print("5. Hæta")
    val = int(input("hvaða lið velurðu ?"))

    
    print("----------------------------------")

    if val == 1:
        tala = []
        margfeldi = 1
        for x in range(50):
            tala.append(random.randint(5,70))
        for y in tala:
            margfeldi = margfeldi * x
        print(margfeldi)    
        print(max(tala))
        print(min(tala))
        print(tala)
        tala.sort()
        print(tala)
        print('--------------------------------------')

    elif val == 2:
        tala1 = []
        for x in range(2000, 3200):
            if x % 7 == 0 and x %5 !=0:
                tala1.append(x)
        for x in tala1:
                print(x, end=',')
        print()
        for i in range(len(tala1)):
            if i != len(tala1) - 1:
                print(tala1[i], end=',')
            else:
                print(tala1[i])
                print('--------------------------------------')

    elif val == 3:
        listi = []
        teljari = 0
        teljari2 = 0
        for i in range(10):
            listi.append(input('segðu orð'))
        for ord in listi:
            if len(ord) == 4:
                teljari = teljari + 1
                print('fjöldi orðanna sem hafa fjöldi stafi er' , teljari)
        for x in range(0 , len(listi), 2):
             print(listi[x][::-1])
        listi.sort()
        print(listi)
        stafur = input('veldu staf til að eyða þeim sem byrja með stafnum ')
        for ord in listi:
            if ord[0] == stafur:
                listi.remove(ord)
            teljari2 = teljari2 + 1
            print(teljari2)
            print(listi)
            print('--------------------------------------')


    elif val == 4:
        listi = []
        teljari = 0
        teljari2 = 0
        for i in range(7):
             listi.append(input('segðu orð'))
        for ord in listi:
            print(listi)
            
        for i in range(6):
             listi.append(input('önnur orð'))
        for ord in listi:
            print(listi)
            
