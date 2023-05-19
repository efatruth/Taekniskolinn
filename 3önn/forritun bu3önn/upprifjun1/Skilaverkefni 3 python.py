from random import*
'''
livinus felix bassey
03.10.2017
Skilaverkefni 3
'''

val = -1
while val != 4:

    print('.................')
    val=int(input('hver lið velðu ?'))

    if val == 1:
        teljari1=0
        tuple_dansherra = ('óláfur', 'ílma', 'viljam', 'danni', 'safi', 'jón')
        tuple_domurnar = ('elsa', 'rósa', 'helga', 'sofia', 'erún', 'lovisa')
        for nafn in tuple_dansherra:
            print(nafn, end=" ")
        print()
        for nafn in tuple_domurnar:
            print(nafn, end=" ")
        print()
        print('.................')

        for i in range(6):
            print('%s og %s'% (tuple_dansherra[i],tuple_domurnar[i]))
        print()



    #dæmi 2
    elif val == 2:
        nöfnsima_dict={'aron':7701230,'afe':7701231,'totti':7701232,'diogo':7701233,'reuben':7701234,'pétur':7701235,'gústi':7701236,'steina':7701237,'bjarni':7701238,'hofni':7701239,}
        nafn=input('sláðu inn nafn: ').lower()
        if nafn in nöfnsima_dict: #virkar
            print(nöfnsima_dict[nafn])

        if nafn not in nöfnsima_dict:#virkar
            print('þetta nafn ekki til í símaskránni ')

    #dæmi 3 ,age of students are values
    elif val == 3:
        nafnaldur_dict={'buba':18,'josh':17,'dafe':18,'ebo':17,'caleb':18,'sam':18,'okoro':17,'kwaku':18,'wele':17,'hope':18,'medi':18,'nonso':17,'elor':17,'ewa':18,'lati':18,}
        print(nafnaldur_dict.keys())
        print()
        for x in nafnaldur_dict:
            print(x,' : ',nafnaldur_dict[x])
        for x in nafnaldur_dict:
            if nafnaldur_dict[x] >= 18:
                print(x,' : ',nafnaldur_dict[x])

        print(nafnaldur_dict.keys())
