#livinus felix bassey
#22.8.2017
val=input("Veldu verkefni 1-6")
#Dæmi eitt
if val =="1":
    tala1=int(input("slaðu inn tölu eitt"))
    tala2=int(input("slaðu inn tölu tvö"))
    #Útreikningar
    plus=tala1 + tala2
    margfald=tala1* tala2
    print ("Niðurstaða fyrir plus er",plus,"n/nNiðurstadas fyrir margfalda er",margfald)

elif val =="2":
    fornafn=input("sláðu inn fornafn ")
    eftirnafn=input("sláðu inn eftirnafn ")
    # Útreikningar
    print("hallo", fornafn,eftirnafn)

elif val =="3":
    km=float(input("sláðu inn lengd í kílómetrum"))
    # Útreikningar
    metrar=km*1000
    print(km,"kílometrar eru ", format(metrar, ".05f"),"metrar" )

elif val =="4":
    laun=int(input("Hvað eru laun? "))
    kl=int(input("hvað ertu að vinna marga kl? "))
    # Útreikningar
    cash=laun*kl
    print("Heildalaun verða þá",cash)

elif val =="5":
    laun = int(input("Hvað eru laun? "))
    kl = int(input("hvað ertu að vinna marga kl? "))
    # Útreikningar
    cash = laun * kl
    if cash > 30000:
        tax=(cash-30000)*0.2

    print("Heildalaun verða þá",cash)
    print("skattur",tax,"krónur")

elif val =="6":
    gradur = int(input("hvað eru gráðurnar margar? "))
    hringir=gradur//360
    afgangu = gradur%360
    print("gradur, og hringir")

