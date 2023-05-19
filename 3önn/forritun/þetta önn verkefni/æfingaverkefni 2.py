# Livinus Felix Bassey
# 18.1.2017
# æfingaverkefni 2

#Liður eitt
tala1=int(input("sláður inn tölu eitt "))
tala2=int(input("sláður inn tölu tvö "))
if tala1 > tala2:
    print("Tala tvö er minni")
elif tala1 < tala2:
    print("Tala tvö er minni")
else:
    print("Tölurnar eru jafn stórar")

#Liður tvö
manudur=input("sláður inn nafn mánaðar ").lower()

if manudur=="janúar":
    print("þetta er fyrsti mánuður ársins")
elif manudur=="febrúar":
    print("þetta er annar mánuður ársins")
elif manudur=="mars":
    print("þetta er þríðji mánuður ársins")
elif manudur=="apríl":
    print("þetta er fjóðji mánuður ársins")
elif manudur=="maí":
    print("þetta er fimmti mánuður ársins")
elif manudur=="júni":
    print("þetta er sjötti mánuður ársins")
elif manudur=="júlí":
    print("þetta er sjöundi mánuður ársins")
elif manudur=="ágúst":
    print("þetta er áttundi mánuður ársins")
elif manudur=="september":
    print("þetta er níundi mánuður ársins")
elif manudur=="október":
    print("þetta er tíundi mánuður ársins")
elif manudur=="nóvember":
    print("þetta er ellefti mánuður ársins")
elif manudur=="desember":
    print("þetta er tólfti mánuður ársins")
else:
    print("Ég þekki ekki þennan mánuð")

#Liður 3
aldur=int(input("Sláðu inn aldur "))
if aldur <= 6 and aldur >=0:
    print("Nú, svo ferð þú að byrja í skóla")
elif aldur <= 15 and aldur >=7:
    janei=input("Ætla þú í menntaskóla ")
    if janei=="já":
        print("Frábært ")
elif janei=="nei":
        print("Jæja þá, það er fint ")
elif aldur <=105 and aldur >16:
    print("Gangi þér vel í framtíðinni")
else:
    print("þú hefur svara spurningunni vitlaust")

#Liður 4
tala=int(input("Sláðu inn tölu á milli 0 og 25 "))
if tala <=24 and tala >=1:
    utkoma=(tala*1.7)
    print(utkoma)
elif tala <=0 or tala >= 25:
    print("Rángur innsláttur")

#Liður 5
brandari=input("Viltu heyra brandara? ")
if brandari=="já":
    print("Ung móðir var að segja vinkonu sinni frá syni sínum."
          "Hann Óli minn er nú orðinn tveggja ára og"
          "hann er búinn að ganga síðan hann var níu mánaða."
          "Vinkonan rak upp stór augu:þú segir ekki!!!,"
          "Blessaður drengurinn,"
          "óskap hlýtur hann að vera orðinn þreyttur!!!")
elif brandari=="nei":
    print('þú um það')
