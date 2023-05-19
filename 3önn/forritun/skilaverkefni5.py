# livinus felix bassey
# 08.3.2017
# skilaverkefni 5

val = 0
while val != 4:
    print('1. kennitala')
    print('2. búa til nýt orð')
    print('3. sneið af streng')
    print('4. hætta')
    val = int(input('hvaða lið veluðu'))

    print('-------------')
    # notanda hefur valið lið eitt ,   jafna er kannski frekar löng en hún virka þó
    if val == 1:
    # hér í while lýkkju ef ske kynni að notanda slá ekki inn rétt kennitölu
        rangt = True
        sneidar = 0
    # og leyfir forritið notandi að slá ekki inn herri tölu nema tíu
        while rangt == True:
            print('1. settu inn tölu ef þú átt að setja eitthvað inn')
            kennitala = input('settu inn kennitölu áðeins með tíu tölum')
            # þá kemur upp rangur innsláttur
            if len(kennitala) != 10:
                print('Rangur innsláttur')
            else:
                # svo geta komið upp allskyns villuskilaboð sem jafnan meðtekur
                tolustafur = True
                for staf in kennitala:
                    if not staf.isdigit():
                        #ef ske kynni til dæmis að notandi slái inn bókstaf þar sem inter ekki á jöfnunni
                        print('kt inniheldur bókstaf')
                        tolustafi = False
                if tolustafur == True:
                    # hérna skoðar svo jafnan hvort allir tölustafir séu skráðir rétt         
                    if int(kennitala[0:2]) < 32:
                        print('fyrstu tveir stafirnir eru Réttir')
                        # og ef svo er þá bætir hann við sneið sem er sett inn til að taka inn tölurnar og hækkar um einn við það    
                        sneidar = sneidar +1
                    if int(kennitala[2:4]) < 13:
                        print('seinna tveir stafirnir eru Réttir')
                        sneidar = sneidar +1
                    if int(kennitala[-1]) == 0 or int(kennitala[-1]) == 9:
                        print('aftasti stafurinn eru réttur')
                        sneidar = sneidar + 1
            if sneidar == 3:
                # ef sneidar jafnan verður að þrem í lokinn hefur kennitalan farið að óskum og verið skrifuð rétt             
                print('kennitala er Rétt')
                rangt = False
                print('----------------------')
#hérna hefur notandi valið lið 2            
    elif val == 2:
        #forritið biður um 5 stafa orð en er það þó ekki alveg skylt
        ord = input('skáðu orð sem inniheldur að minnsta kosti 5 stafi')
        # hún tekur svo 2 stafi af byrjum orðs og tvo stafi                  
        nyttord = ord[0:2] + ord[-2:]
# Hér þá prentast strengurinn út
        print('nýji strengurinn er', nyttord)
# svo þá er hann settur í upper string til að fá hann í hástöfum
        nyttord = nyttord.upper()
        print('orðið í hástöfum', nyttord)
# og einnig svo hann prentist í lágstafi með string lower
        nyttord = nyttord.lower()
        print('orðið í lágstöfum', nyttord)
        print('---------------------')
    elif val == 3:
# hér skrifar notandi inn nafn
        nafn = 0
        nafn = input('sláðu inn nafn ')
# setur nafnið síðan í lykkju
        for i in range(len(nafn)):
            print(nafn[i:])
        print('-----------------------')
# Hérna þakkar forritið fyrir samveruna og slekkur svo á forritinu
    elif val == 4:
        print('Takk fyrir samveruna notandi')
        val = 4
                              

        
