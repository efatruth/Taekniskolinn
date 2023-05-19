#livinus felix bassey
#13.03.2017
#hlutapróf 2

tolur = "já"
val = 0
while val != 5:
    print ("1. heiltolu")
    print ("3. valdatolur")
    print ("3. sentimeter")
    val = int(input("hvern liður veluður"))
    print (".....")

    if val == 1:
        tolur = "já"
        while tolur == "já":
            senti = int(input("sladur toluna í sentimetrum"))
            metri = senti // 100
            afg = senti % 100
            desi = afg // 10
            afg = afg % 10
            senti = afg // 1
            print("þetta eru ",metri, "metrar")
            print("þetta eru ",desi, "desimetrum")
            print("þetta eru ",senti, "sentimetra")
            tolur = input("viltur gera þetta aftur já /nei ?")
            print (".....")


    if val == 2:
        tolur = "já"
        while tolur == "já":
            X = int(input("hvaða toluna veludu ?"))
            n = int(input("hvað er veluði ?"))
            veldi = X**n
            print ("veldi")
            tolur = input("viltur gera þetta aftur já /nei ?")
            print (".....")


    if val == 3:
        tolur = "já"
        while tolur == "já":
            stjarna = int(input("sladur tölu á bilinu 1 - 9 "))
            if stjarna <= 9:
                tolur = "já"
            star1 = "*"
            star2 = "*"
            for y in range(stjarna, 0):
                y +=1
                print("*" * (0-y+1))
            for n in range(0,stjarna):
                n +=1
                print ("*" *(0-n+1))
                 
    elif val == 4:
                    print ("þakk kæera")

            
    


              
        
             
            
            
