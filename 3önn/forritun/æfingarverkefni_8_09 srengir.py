# livinus felix bassey
# 08.3.2017
#09 Æfingarverkefni - strengir


val = 0
while val != 5:
    print("a. lengsta ordið")
    print("b. random tolur")
    print("c. telja ordid")
    print("d. afturábak")
    val = int(input("hvaða lið veluðu"))

    print("--------")
    if val == 1:
        print("skrifar 2 orð og forritið finnur svo hvert er lengst")
        nafn1 = input("segðu eitt orð ")
        nafn2 = input("segðu annað orð")

        for X in range(len(nafn1)):
            print(X)
        print(nafn1, ':', len(nafn1))
        for Y in range (len(nafn2)):
            print(Y)
        print(nafn2, ':', len(nafn2))

        if (len(nafn1)) > (len(nafn2)):
            print("þetta ord er lengra", nafn1)
        elif(len(nafn1)) < (len(nafn2)):
            print("þetta ord er lengra", nafn2)
    print("-------")
    if val == 2:
        nafn = input("skrifar inn nafn þitt")
        nafn = nafn.upper()
        print(nafn)
        nafn = nafn.lower()
        print(nafn)
        stafur = input("veldu staf til að breyta í * ")
        tala = int(input("hve morgum af stofunum viltu breyta ?"))
        nafn = nafn.replace(stafur,"*", tala)
        print("hena er nafnið breytt:", nafn)
        print("----------------")


    if val == 3:
        orð = input("veldu þer orð ")
        orð = (len(orð))
        print("það eru ", orð, "°stafir í orðinu sem þú valdir")
        print("---------")
    elif val == 4:
        setning = input("settu inn setningu")
        print("hérna er það bæði fram og áfturábak", setning, setning[::-1])
        print("---------")

    elif val == 5:
        print("sjáumst seinna notandi")
        val = 5
            
        
        

    

        


    
        

    
