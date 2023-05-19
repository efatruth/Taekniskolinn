#livinus felix bassey
#12.9.2017
#skilaverkefni föll

#fallið farenheit, breytir celsius í farenheit
def celcius_farenheit(cels):
    farenh = cels * 1.8 +32
    return farenh
#fallið celsius, breytir farenheit í celcius
def farenheit_celcius(farenh):
    cels = (farenh -32)/1.8
    return cels
#hér koma föllin hvert af öðru til dæmis
#fallið kelvin, breytir celsius í kelvin
def celsius_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin
#fallið celcius, breytir kelvin í celsius
def kelvin_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

#prófum við föllin með því að kalla í þau
val = -1
while val != 0:
    print("valmynd:")
    print("1. breyta celcius í farenheit eða öfugt.")
    print("2. breyta celcius í kelvin eða öfugt.")
    print("3. grunntölu og veldi.")
    print("4. breytir tommum yfir í sentimetra og öfugt.  ")
    print("5. breytir gallonum í lítra og öfugt ")
    print("6. nafn notanda og  kyn(kk/kvk).")
    print("7. aðferðina kasta(). ")
    print("8. tvo lista. ")
    print("0. til að hæta.")
    val = int(input("veldu lið úr valmynd?."))
    #eftir að búið er að taka við vali er farið í viðkomandi lið með if, elif og else
    if val == 1:
        print('þú hefur valið lið 1')
        svar = input("vedu a ef þú vilt breyta celcíus í farenheit\n eða B ef þú vilt breyta farenheit í celsíus").upper()
        if svar == "A":
            hiti_c = float(input("hvað er hitinn í celcius ?"))
            #kalla falli í celcius fahrenheit til að reikna
            hiti_f = celcius_farenheit(hiti_c)
            print(str(hiti_c) + "°C er" + format(hiti_f, ".2F") + "°F")
        elif svar == "B":
            hiti_f = float(input("hva er hitinn í farenheit ?"))
            #kalla í falli fahrenheit celcius til að reikna
            hiti_c = farenheit_celcius(hiti_f)
            print(str(hiti_f) + "°F er" + format(hiti_c, ".2F") + "°C")

            
    elif val == 2:
        print('þú hefur valið lið 2')
        
        svar = input("vedu a ef þú vilt breyta celcíus í kelvin\n eða B ef þú vilt breyta kelvin í celsíus").upper()
        if svar == "A":
            hiti_C = float(input("hvað er hitinn í celcius ?"))
            #kalla í falli celcius kelvin til að reikna
            hiti_k = celsius_kelvin(hiti_C)
            print(str(hiti_C) + "°C er" + str(hiti_k, ".2F") + "°k")
        elif svar == "B":
            hiti_k = float(input("hvað er hitinn í kelvin ?"))
            #kalla í falli kelvin celcius til að reikna
            hiti_C = kelvin_celsius(hiti_k)
            print(str(hiti_k) + "°k er" + str(hiti_C, ".2F") + "°C")


    elif val == 3:
        def veldi(x, veldi):
            utkoma = 1
            for n in range(int(veldi)):
                utkoma = utkoma * x
            return utkoma

        grunnt = float(input("Hver er grunntalan? "))
        veldist = float(input("Hvaða veldi? "))
        tala_i_veldi = veldi(grunnt, veldist)
        print(grunnt, "í veldinu", veldist, "er", tala_i_veldi)

    elif val == 4:
        def tomma_sentimetra(tomma):
            sentimetra = tomma * 2.54
            return sentimetra

        def sentimetra_tomma(sentimetra):
            tomma = sentimetra / 2.54
            return tomma
        print('þú hefur valið lið 4')# hérna er tomma í sentimetrar
        svar = input("vedu a ef þú vilt breyta tommum í sentimetra\n eða B ef þú vilt breyta sentimetra í  tommum").upper()
        if svar == "A":
            tommur = float(input("hvað eru margar tommur ?"))
            # kalla í falli tommum sentimetra til að reikna
            sentimetrar = tomma_sentimetra(tommur)
            print(str(tommur) + " tommum er" + str( sentimetrar, ".2F") + "sentimetrar")


        elif svar == "B":
            sentimetrar = float(input("hvað eru margar tommur ?"))
            # kalla í falli tommum sentimetra til að reikna
            tommur = sentimetra_tomma(sentimetrar)
            print(str(sentimetrar) + " sentimetrar eru" + str(sentimetrar, ".2F") + "tommur")

    

    elif val == 5:
        print('þú hefur valið lið 5')
        #hérna er gallon í litrar
        def gallon_litra(gal):
            litra = gal * 3.785
            return litra

        #hérna er litrar í gallon
        def litrar_gallon(litra):
            gal = litra / 3.785
            return gal


    elif val == 6:
        print('þú hefur valið lið 6')
        def nafn_kyn(nafn,kyn):
            if kyn == "kk":
                return "sæll og blessaður", nafn
            elif kyn == "kvk":
                print('sæl og blessuð', nafn)

            
