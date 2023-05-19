#livinus felix bassey
#26.04.2017
#hlutapróf33

import random
aftur = "já"
val = 0
while val != 4:

    print("1. skrifa út tölurnar 200-400 í eina línu")
    print("2. vinna með tilviljanakenndar (random)tölur.")
    print("3. vinna með texti (streng)")
    print("4. hæta")
    val = int(input("hvaða lið velurðu ?"))

    print('-----------------------------------')
    
    if val == 1:
        for x in range(200,400+1):
            print(x)


    if val == 2:
        listi = []
        for x in range(100):
            listi.append(random.randint(2000,2030))
        print("meðaltal talnanna ",format(sum(listi)/len(listi),".1f"))
        print(listi.count(2005))
        for x in listi:
            if x > 2020:
                print(x, end=' ')
        print()


        
