import random
'''
livinus felix bassey
19.02.2018
Skilaverkefni 3
'''
#.........Danspörin föll...........#
def prenta_Tuple(tup):
    for x in tup:
        print (x, end=" ")

def paraRod(tup1, tup2):
    for x in range(len(tup1)):
        print(tup1[x], "and", tup2[x])

#?
def paraRandom(tup1, tup2):
    for x in range(len(tup1)):
        print(tup1[random.randint(0,5)], "og", tup2[random.randint(0,5)])

def paraRandomStrakur(tup1, tup2):
    kk = random.sample(tup1,len(tup1))
    kvk = random.sample(tup2,len(tup2))
    for x in range(len(tup1)):
        print(kk[x], "og", kvk[x])
#til

def finnaOllNofn(stafur, tup1, tup2):
    ollNofn=[]
    for x in tup1:
        if stafur in x:
            ollNofn.append(x)
    for x in tup2:
        if stafur in x:
            ollNofn.append (x)
    return ollNofn

def finnaNafn(stafur, tup2):
    nafnalisti=[]
    for x in tup2:
        if stafur == x[0]:
            nafnalisti.append(x)
    return nafnalisti

#?
def baedi_tup(nafn1, nafn2):
    nafnlisti3=[]
    for x in nafn1:
        if x.count("n") > 1:
            nafnlisti3.append(x)
    for x in nafn2:
        if x.count("n") > 1:
            nafnlisti3.append(x)
    return nafnlisti3


tuple_dansherra = ('óláfur', 'ilma', 'viljam', 'danni', 'safi', 'jón')
tuple_domurnar = ('enna', 'rósa', 'helga', 'sofia', 'erún', 'lovisa')

#............föll fyrir Símaskrá..........#
def nafnDict(keyVal):
    if nafn in keyVal:  # virkar
        print(keyVal[nafn])

    if nafn not in keyVal:  # virkar
        print('þetta nafn ekki til í símaskránni ')

nöfnsima_dict = {'aron': 7701230, 'afe': 7701231, 'totti': 7701232, 'diogo': 7701233, 'reuben': 7701234,'pétur': 7701235, 'gústi': 7701236, 'steina': 7701237, 'bjarni': 7701238, 'hofni': 7701239, }


#..........hérna er föll Skráning í bekk........#
def allNema(nem):
    for x in nem:
        print(x, nem[x])


def nemAldur(nem):
    for x in nem:
        if nem[x] >= 18:
            print(x,' : ',nem[x])

def medalAldur(nem):
    talnalisti = []
    for x in nem:
        talnalisti.append(nem[x])
    return round(sum(talnalisti) / len(talnalisti), 2)

def heilAldur(nem):
    heildaraldur = 0
    for x in nem:
        heildaraldur = heildaraldur + nem[x]
    return heildaraldur

def stafAldur(nem,staf):
        aldListi = []
        for x in nem:
            if staf == x[0]:
                aldListi.append(x)
        return aldListi

nafnaldur_dict={'buba':18,'josh':17,'dafe':18,'ebo':17,'caleb':18,'sam':18,'okoro':17,'kwaku':18,'wele':17,'hope':18,'medi':18,'nonso':17,'elor':17,'ewa':18,'lati':18,}

val = 0
while val != 4:
    print("---------------valmynd------------------")
    print("1. Danspörin.")
    print("2. Símaskrá.")
    print("3. Skráning í bekk.")
    print("4. Hætta.")

    val = int(input("Veldu hvað þu´vilt gera"))
    if val ==1:
        svar = input('hérna á að veludu A,B,C,D,E,F')

        if svar.upper() == "A":
            print()
            print("þetta eru dansherrarnir")
            prenta_Tuple(tuple_dansherra)
            print()
            print("þetta eru domurnar")
            prenta_Tuple(tuple_domurnar)
            print()

        elif svar.upper() == "B":
            paraRod(tuple_dansherra,tuple_domurnar)
            print()

        elif svar.upper() == "C":
            paraRandom(tuple_dansherra,tuple_domurnar)
            print()

        elif svar.upper() == "D":
            paraRandomStrakur(tuple_dansherra,tuple_domurnar)
            print()

        elif svar.upper() == "E":
            staf1 = input("slaðu inn staf")
            print(finnaOllNofn(staf1, tuple_dansherra, tuple_domurnar))

        elif svar.upper() == "F":
            staf = input("slaðu inn staf")
            print(finnaNafn(staf, tuple_dansherra))
            print(finnaNafn(staf, tuple_domurnar))

        elif svar.upper() == "G":
            print(baedi_tup(tuple_dansherra,tuple_domurnar))



    elif val ==2:
        nafn = input('sláðu inn nafn: ')
        print(nafnDict(nöfnsima_dict))


    elif val ==3:
        svar = input('hérna á að veludu A,B,C,D,E,F')

        if svar.upper() == "A":
            allNema(nafnaldur_dict)
            print()
        elif svar.upper() == "B":
            nemAldur(nafnaldur_dict)

        elif svar.upper() == "C":
            print("Meðalaldur er:",medalAldur(nafnaldur_dict))

        elif svar.upper() == "D":
            print("Heildaraldur er", heilAldur(nafnaldur_dict))

        elif svar.upper() == "E":
            staf = input("slaðu inn staf")
            print(stafAldur(nafnaldur_dict, staf))


    elif val ==4:
        pass
    else:
        print("Eitthvað rangt valið")
