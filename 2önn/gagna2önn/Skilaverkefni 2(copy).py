# Livinus Felix Bassey
# 03.2.2017
# Skilaverkefni 2


loop = "j" #loopan fyrir while loop
listi = []


val=""

while loop == "j": #Valmynd kemur upp í loopu meðan loop er "j"
    print("[1] Bæta við nýjum í símaskránna.")
    print("[2] Breyta upplýsingum í símaskránni.")
    print("[3] Eyða upplýsingum / eyða línu úr símaskránni.")
    print("[4] Prenta út alla símaskránna ein lína per notanda")
    print("[5] Leita að ákveðnu nafni og prenta upplýsingar um það nafn, sima og kennitölu")
    print("[6] CSV já byrja")
    print("[7] Hætta.")
    val = input("sláður inn númerið sem þér langar að velja: ")#spyr um að velja val
    

    if val == "1":
        
        file = open("simaskra.txt","a") #Byr til / Bætir í skjalið með "append" 
        rangeval = int(input("Hver margar langar þér að bæta við?: ")) #spurt hversu marga honum langar á
        for i in range(rangeval): #range hversu margir verða bættir
            print("")
            print("")
            print("upplýsingar um vin nr ", (i+1)) #upplýsingar um einstaklinginn
            nafn = input("hvað heitir hann/hún?: ")
            kenni = input("hver er kennitalan?: ")
            simi = input("hvað er simanúmerið?: ")
            nysimaskra = (str(simi)+ "\t|\t" + str(kenni) + "\t|\t" + str(nafn) + "\n") #upplýsingarnar...
            file.write(nysimaskra) #upplýsingarnar verða skrifaðar í skjálið
            listi.append(nysimaskra)#Hver notandi verður settur í lista (listinn er samt ónotaður)
        file.close() #lokað við file-ið

    if val == "2":
      print ("þurfum ekki gera þetta")


    if val == "3":
      print ("þurfum ekki gera þetta")  


    if val == "4":
        file = open("simaskra.txt","r") #hér er verið að lesa úr skjalinu
        print("")
        print ("kennitala \t|\t simanúmer \t|\t Nafn") #print sem sorterar uppýsingarnar
        print("-----------------------------------------------")
        print(file.read())#print út allt sem er í simaskra.txt skjalinu


    if val == "5":
        print ("þurfum ekki gera þetta")

        
    if val == "6":
        import csv
        '''f = open('postnumer.csv')
        csv_f = csv.reader(f)
        for row in csv_f:
          print(row[0])
          '''
        with open('postnumer.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=';')
            for row in readCSV:
                '''print(row)'''
                '''print(row[0])'''
                print(row[0]+"\t",row[1],)

          
    
    if val == "7":
        print ("Forritið hættir")#loopann breytist í h og þá hættir forritið
        loop = "h"
