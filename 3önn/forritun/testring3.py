
#Valmynd
val = 0
while val != "5":
    print("1. Lengsta Orðið")
    print("2. Nafn")
    print("3. Að Telja Orð")
    print("4. Afturábak")
    print("5. Hætta")
    val = input("Veldu lið ")
    #Liður 1
    if val == "1":
        print("\n<-----Liður 1----->")
        print("Núna verður þú beðinn um að skrifa fimm nöfn")
        listi = []
        for x in range(5):
            nafn = input("Skrifaðu inn eitt nafn ")
            listi.append(nafn)
        lengstanafn = max(listi,key=len)
        print("Lengsta nafnið er =",max(listi, key=len),"og er það",len(lengstanafn),"stafir")
        print()
    #Liður 2
    elif val == "2":
        print("\n<-----Liður 2----->")
        nafn = input("Hvert er nafn þitt ungi maður? ")
        nafn2 = nafn.upper()
        print(nafn2)
        nafn2 = nafn.lower()
        print(nafn2)
        stafur = input("Veldu einn staf sem er í nafni þínu ")
        print(nafn.replace(stafur, "@"))
        print()
    #Liður 3
    elif val == "3":
        print("\n<-----Liður 3----->")
        strengur = input("Skrifaðu setningu ")
        print("Það eru ",len(strengur.split()),"orð í þessari setningu")
        print()
    #Liður 4
    elif val == "4":
        print("\n<-----Liður 4----->")
        setning = input("Skrifaðu setningu ")
        print(setning[::-1])
        print()
    #Liður 5
    elif val == "5":
        print("\nOkay bye bye")
    else:
        print("\nVeldu 1,2,3,4 eða 5. Ekki",val)
        print()
