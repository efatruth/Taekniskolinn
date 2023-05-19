# Livinus Felix Bassey
# 03.2.2017
# Hlutaprof 1

#liður1
#hérna er nótanda upplysingar
nafn = input("hvað heitiðu?")
litur = input("hvað úpphaldsliturinn þinn?")
stræto = input("hvaða stræto tekur ?")

print("Góðan dag" ,nafn, "upphalds liturinn þinn er ", litur, "og þú tekur stræto oftast numer", stræto)

#liður2
#hérna er hæð notanda í sentimetrum  
hæd = int(input("hvað er há/hár þinn í sentimetrum ?"))
if hæd <=147:
    print("smá vaxin eða barn")
else:
    print("Alltaf að vaxa ")
if hæd > 251:
    print("Nei nú lýgur þú!")

#liður3
#hérna eru reikningur tölur 
tala1 = int(input("hvað er fyrsta talan ?"))
tala2 = int(input("hvað er önnur talan?"))
tala3 = int(input("hvað er þriðja talan ?"))

print(tala1 *(tala2 + tala2))


#liður4
#hérna er reikningna flatarmál, ferhyrnings,þríhyrnings eða hrings
spur = int(input("hvað er há/hár þinn í sentimetrum ?"))
if spur == 1:
    lengd = int(("hvað er lengdinn?"))
    breidd = int(("hvað er breidinn?"))
    print ("flatarmál, ferhyrningsins er ",lengd * breidd)
elif spur == 2:
    hæd = int(input("hvað er hæðinn?"))
    grunnlina = int(input("hvað er grunnlina?")) 
    print ("flatarmál, ferhyrningsins er ",hæd * (grunnlina / 2))
elif spur == 3:
    radíus = int(input("hvað er radíus?"))
    grunnlina = int(input("hvað er grunnlina?")) 
    print ("flatarmál, ferhyrningsins er ",radíus * (3.14))
else:
    print("Rangt valið")










    

