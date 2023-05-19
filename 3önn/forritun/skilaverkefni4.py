# livinus felix bassey
# 15.2.2017
# skilaverkefni4

#liður 1

svar = "já"
lið = 1
while lið != 5:
    print('1 - oft sláður heiltölur')
    print('2 - hlaupár')
    print('3 - margfölður ')
    print('4 - heilatólu')
    print('5 - hæta')
    lið = int(input('hvað viltu byrja'))
    '''while val !=5:
    print('# heilatólu endurtaka')
    print('# hláupar')
    print('# tolur + afturtekid ')
    print('# heilatólu')
    print('# hæta')
    val = int(input('hvað lið veluður'))
    print('..')
    if val == 1:
    heiltala1 = int(input('skraðu inn heiltölu'))
    enðurtekid int(input('hversu oft að srai hana'))
    for y in range('enðurtekid'):
        print('heiltala1')
   print('..')


     if val == 2:
     aftur = já


    margf = ''
       innstal = int(input('sláður heiltolur'))
       for x i range( innstala):
       margf = margf + "x"
       print(margft)
    


while val !=5:
    print('# heilatólu endurtaka')
    print('# hláupar')
    print('# tolur + afturtekid ')
    print('# heilatólu')
    print('# hæta')
'''
    if lið == 1:
        heiltala = int(input('slaður inn heiltala'))
        oft = int(input('hversu oft viltu sláður inn heiltölu ?'))
        for i in range(oft):
            print(heiltala)

    elif lið == 2:
        artal = int(input('slaður inn artal'))
        if(artal%100 == 0):
            if(artal%400 == 0):
                print('þetta er hlaupár')
            else:
                print('þetta ekki hlaupár')
    
        elif(artal%4 == 0):
            print('þetta er hlaupár')
        else:
            print('þetta ekki hlaupár')



    elif lið == 3:
        margf = 1
        innstala = int(input('sláðu heiltölu'))
        for x in range(innstala, 0, -1):
            margf = margf * x
        print(margf)
   




    elif lið == 4:
        marg = ""
        innstala = int(input('sláðu heiltölu'))
        for x in range(innstala):
            marg = marg + '*'
            print(marg)

    elif lið == 5:
        print('Takk fyrir mig')

    else:
        print('ÆÆ, Eitthvað fór úrskeiðis, reyndu aftur')
