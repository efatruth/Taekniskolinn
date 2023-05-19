# Livinus Felix Bassey
# 03.2.2017
# Hlutapróf 1

loop = "j" #loopan fyrir while loop
listi = []

val=""

while loop == "j": #Valmynd kemur upp í loopu meðan loop er "j"
    print("1. Bæta í skrána.")
    print("2. Birta skána í heild sinni.")
    print("3. Eyða upplýsingar um ákveðið dýr eftir nafni þess.")
    print("4. Hætta ")
    val = input("sláður inn númerið sem þér langar að velja: ")#spyr um að velja val


    if val == "1":
        
        file = open("textaskranni.txt","a") #Byr til / Bætir í skjalið með "append" 
        rangeval = int(input("Hver margar langar þér að bæta við?: ")) #spurt hversu marga honum langar á
        for i in range(rangeval): #range hversu margir verða bættir
            print("")
            print("")
            print("upplýsingar um gæludýr og eiganda nr ", (i+1)) #upplýsingar um einstaklinginn
            eiganda = input("hvað heitir þú?: ")
            gæludýr = input("hvað heitir gæludýr þitt?: ")
            tegund = input("hvað tegund gæludýr(hundur/köttur osfrv)?: ")
            nytextaskranni = (str(eiganda)+ "\t|\t" + str(gæludýr) + "\t|\t" + str(tegund) + "\n") #upplýsingarnar...
            file.write(nytextaskranni) #upplýsingarnar verða skrifaðar í skjálið
            listi.append(nytextaskranni)#Hver notandi verður settur í lista (listinn er samt ónotaður)
        file.close() #lokað við file-ið




    if val == "2":
        file = open("textaskranni.txt","r") #hér er verið að lesa úr skjalinu
        print("")
        print ("eiganda \t|\t gæludýr \t|\t tegund ") #print sem sorterar uppýsingarnar
        print("-----------------------------------------------")
        print(file.read())#print út allt sem er í textaskranni.txt skjalinu
        loop = "h"
        


