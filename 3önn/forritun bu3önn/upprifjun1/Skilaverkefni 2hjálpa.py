#livinus felix bassey
#12.9.2017
#skilaverkefni föll

#fallið farenheit breytir celsius í farenheit
def celcius_farenheit(cels):
    farenheit_celcius =cels * 1.8 +32
    return farenh
#fallið celsius breytir farenheit í celcius
def celcius(farenh):
    cels = (farenh -32)/1.8
    return cels
#hér koma föllin hvert af öðru til dæmis
#celsius_kelvin(celsius):
#kelvin_celsius(kelvin):

#prófum við föllin með því að kalla í þau
val = -1
while val != 0:
    print("valmynd:")
    print("1. breyta celcius í farenheit eða öfugt.")
    print("2. breyta celcius í kelvin eða öfugt.")
    #og svo framvegis upp í lið 8
    print("0. til að hæta.")
    val = int(input("veldu lið úr valmynd?."))
    #eftir að búið er að taka við vali er farið í viðkomandi lið með if, elif og else
    if val == 1:
        svar = input("vedu a ef þú vilt breyta celcíus í farenheit\n"
                     "eða B ef þú vilt breyta farenheit í celsíus").upper()
        if svar == "A":
            #kalla falli í celcius til að reikna
            hiti_c = float(input("hva er hitinn í celcius ?"))
            hiti_f = celcius (hítí_c)
            print(str(hiti_c) + "°C er" + format(hiti_f .2F) + "°F")
        if svar == "B":
            hiti_f = float(input("hva er hitinn í farenheit ?"))
            #nú klarið þíð verkefnið
        else:
            #allt annað en A eða B
            print("ég skil ekki")
            #elif val fyrir liði 2 til 8
            #enda á elif == 0 til að hætta og else sem skrifar villubod
        elif val == 0:
            print("takk fyrir að nota forritið.")
        else:
            #allt annað en þegar hefur verið skoðað
        print("þessi liður er ekki til.")
