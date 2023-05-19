'''
Livinus Felix Bassey
18.1.2017
Skilaverkefni 1, æfingar í að taka uppýsingar og skila niðurstöðum á skjá
'''

print("Liður 1") #Hérna þá byrja fyrsti verkefni liðurinn í verkefni
#hérna þá skráir notandi inn nafnið eitt
Nafn = input("hvað er nafnið þitt notandi")
#svo það er hægt að nýta það í þessum hérna liði
print("Velkoming í áfanga FORITÖBAU " + Nafn + "þetta verður skemmtileg önn")


print("Liður 2") #hér er svo liður 2
#hérna skrái ég inn kommutölu
kommutala = float(input('Sláðu inn kommutölu með 3 aukastöfum'))
#svo þá prentast hún út með aðeins einni kommutölu
print("þú hefur valið töluna" + (format(kommutala,".1f")))


print("Liður 3") #hérna er liður 3
tala1 = int(input("Hver er fyrsta heiltalan")) #Hérna setur notandi inn fyrstu tölu
tala2 = int(input("Hver er önnu heiltalan")) #og svo seinn
margfeldi = tala1 * tala2 # margfalda
print(margfeldi) #prenta margfeldi
minus = tala1 - tala2 #minus
print(minus) #prenta minus


print("Liður 4") #Liður númer 4
h = int(input("hver er hæðinn")) #hérna skrifar notandi inn hæðina
b = int(input("hver er breiddinn")) #hérna breiddinna
l = int(input("hver er lengdinn")) #og hérna kemur lengdinn
rummal = h * b * l #hérna þá * á þér til samans
print(rummal) #og penta þér síðan út


print("Liður 5") #liður 5
notandialdur = int(input("hve gamall ertu?"))
pabbaaldur = int(input("hve gamall er faðir þinn?"))
Aldur = pabbaaldur - notandialdur
print("pabbi þinn hefur verið sirka" + str(Aldur) + "þegar þú fæddist")


print("Liður 6") #liður 6
Aldur1 = int(input("Hver er aldur 1"))
Aldur2 = int(input("Hver er aldur 2"))
Aldur3 = int(input("Hver er aldur 3"))
utkoma = Aldur1 + Aldur2 + Aldur3
print("Hérna er meðalaldur" + str(utkoma) + "hjá þeim")

print("Gaman að geta aðstoðað þig við þessa útreikninga")
