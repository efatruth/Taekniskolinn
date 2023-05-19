# livinus felix bassey
# 15.2.2017
# skilaverkefni í while lykkjum

svar = "já" #þertta er sé liður sem ég myndi nota ef þurfti í liðum.
val = "já" # þetta er sé sem reður yfir while lykkjunni.
valmynd = 'já' #breyta sem notu er til að endurtaka while lykkju. 
while val == 'já': # while lykkju byrja hér # valmynd sem er  endurtekinn.
    print ('1. slá inn heiltölu')
    print ('2. reikna flatarmál ferhyrnings.')
    print ('3. leyniorð')
    print ('4. heiltala í fimm sinnum töflur')
    print ('5. suma, meðaltal , jofn eða odds, ásamt meira')
    val = int(input('hvað viltu gera'))

    #liður 1 verkar þanning að þú skrifa inn tölu og síðan prenta hanna út. forritið spyr
    if val == 1:
        while svar == "já":
            print('þú hefur valið lið 1')
            tala1 = int(input('sláður inn heiltalan: '))
            print('þú valdir toluna', tala1)
            svar = input('viltu setja inn aðra (já/nei)')
        print('takk fyrir að nota forritið egðu goðan dag / nótt')
        
        

    #liður 2 hér þá ef ég buið til forritskóða til að finna flátarmál ferhyrnings
    if val == 2:
        while svar == 'já':
            lengd = int(input('hvar er lengd ferhyrningsins'))
            breidd = int(input('hvar er breidd hans'))
            flatarmal = lengd * breidd
            print('flatarmálið er' ,flatarmal)
            svar = input('viltu gera þetta aftur  (já/nei)')
            print ('tákk fyrir')
        print('takk fyrir að nota forritið egðu goðan dag / nótt')
        


    #liður 3 
    if val == 3:
        while svar == 'já':
            leyni = (input('hvar er leyniorðið'))
            leyniord = 'leyni'
            if leyni == leyniord:
                print('þú fannst það , jibbi')
                svar = input('viltu gera þétta aftur (aftur/nei)')
            else:
                print ('þú náðir ekki leynorðinu reyndu aftur')
                svar = 'aftur'
        print('takk fyrir að nota forritið egðu goðan dag / nótt')


    #liður 4 hérna þá slærðu inn aðra heiltölu og er svo athugað hvort talan er í 5 * töflunni
    if val == 4:
        svar = 'endurtaka'
        while svar == 'endurtaka':
            heiltala2 = int(input('sláður inn heilatölu'))
            if heiltala2 % 5 == 0:
                print('Rétt hjá þér')
                svar = input('viltu fá að endurtaka þétta endurtaka/nei')
            else:
                print ('Talan sem skrifuð var inn er ekki í fimm sinnum töflunni')
                svar = 'endurtaka'

    
    #liður 5 1 liði fimm áttu þá býr forritið til nýja while lykkju
    if val == 5:
        valmynd = 'já'
        while valmynd == 'já':
            #sem leyfir notanda að velja mill þess að finna summu og meðaltal 10 talna  sem hann 
            print('1 - summa og meðaltal')
            #hvort hann vilji finna slétta eða oddatölu
            print('2 - jafn eða oddatalan')
            #eða hætta og þá skrifar forritið í leiðinni ég er frábær forritari
            print('3 - hætta og er frábær forritari 10 sinnum')
            lidir = int(input('hvaða lið viltu velja'))
            
            if lidir == 1:
                tolur = int(input('sláður fyrsta heiltölu'))
                Tolur = int(input('sláður annan heiltölu'))
                tOlur = int(input('sláður þriðju heiltölu'))
                toLur = int(input('sláður fjórða heiltölu'))
                tolUr = int(input('sláður fimmta heiltölu'))
                toluR = int(input('sláður sjötta heiltölu'))
                TOlur = int(input('sláður sjöunda heiltölu'))
                tOLur = int(input('sláður áttunda heiltölu'))
                toLUr = int(input('sláður níunda heiltölu'))
                tolUR = int(input('sláður tíunda heiltölu'))
                summa = (tolur + Tolur + tOlur + toLur + tolUr + toluR + TOlur + tOLur + toLUr + tolUR)
                medaltal = (tolur + Tolur + tOlur + toLur + tolUr + toluR + TOlur + tOLur + toLUr + tolUR) / 10           
                print('summan þessar tölur eru:', summa)
                print('medaltal þeirra eru:', medaltal)

            if lidir == 2:
                heiltal = int(input('sláðu inn heiltölu'))
                if heiltal % 2 == 0:
                    print('þessi talan er jafntalan')
                    
                elif heiltal % 1 == 0:
                    print('þessi talan er oddatalan')
                else:
                    print('sláðu töluna, ekki bókstöf')


            if lidir == 3:
                teljari = 1
                while teljari < 11:
                    print('ég er frábær forritari')
                    teljari = teljari + 1
                    break
                
    if val == 6:
        print('munurinn á þessi tveimum kóðonum')
        i = 0           #her null    
        while i != 10:  #svo kemur meðan í er ekki 10
            i = i + 1   #er hækkari um 1
            print (i)   #prenta tölur í hver skipti

        
            #i = 1             Þetta mun fara óendanlega Vegna þess að það er fær yfir númer 10

           #while i != 10:
            #    i = i + 2
            #    print (i)



        
