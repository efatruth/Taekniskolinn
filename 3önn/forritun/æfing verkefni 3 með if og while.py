# livinus felix bassey
# 15.2.2017
# sýnidæmi valmynd með if og while

val = 1 # breyta sem nýtist í valmynd, sett sem 1 til að komast inn í while
# bý til valmynd
while val != 0:
    print('-----------')
    print('Valmynd:')
    print('1. Hringir')
    print('2. Mæting á æfingu')
    print('3.....')
    print('4. millimetrar')
    print('0. Til að hætta') # Þegar notandi velur 0 er hætt í valmynd/forriti
    val = int(input('Veldu númer úr valmynd'))

    # Nú getum við notað if, elif, else til að fara í valinn lið
    if(val == 1):
        # dæmi 1, tek inn gráður og skila heilum hringjum og gráðum
        gradur = int(input('Hvað eru gráðurnar margar? '))
        venjulegDeiling = gradur / 360
        hringir = gradur // 360 # Hér nota ég heiltöludeilingu til að fá heila hringi
        gradurEftir = gradur % 360 # hér nota modulo til að fá afgang af heilum hringjum
        print('Þetta er ekki það sem ég vil fá: ' + str(venjulegDeiling) + ' hringir')
        print('Heldur vil ég hafa þetta svona:')
        print(gradur, 'gráður gera', hringir, 'hringi og', gradurEftir, 'gráður')

    elif(val == 2):
        print('hér kemur það sem á að gera þar')
    elif(val == 4):
        # Stundum þarf að nota afganginn til að finna nýjar tölur
        # dæmi 4 tek við millimetrum og segi hvað eru margir metrar, sentimetrar og mm
        millimetrarInn = int(input('Hvað eru millimetrarnir margir? '))
        metrar = millimetrarInn // 1000 # Það eru 1000 mm í meter
        afgangur = millimetrarInn % 1000 # Þarf að vita hvað margir mm eru eftir
        cm = afgangur // 10 # tek afganginn og deili með 10, þa eru 10 mm í cm
        mm = afgangur % 10  # þá get ég fundið hvað margir millimertar eftir
        print(millimetrarInn, 'mm eru:')
        print(metrar,'metrar,')
        print(cm, 'sentimetrar')
        print(mm, 'mm')
    elif val == 0:
        print('Takk fyrir að nota forritið mitt')
    else:
        print('Þú hefur valið vitlaust númer')
