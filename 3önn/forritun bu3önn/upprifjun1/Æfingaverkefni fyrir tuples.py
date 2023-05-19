'''
livinus felix bassey
26.9.2017
tuples
Æfingaverkefni fyrir tuples
'''

val = -1
while val != 6:
        print('..............valmynd.............')
        print('1.tuple með sex stökum')
        print('2.tuple innheldur 4 lista')
        print('3.tuple innheldur 14 stafi')
        print('4.tuple með tölunum(1,2,3,4,5).')
        print('5.staf og athugar ')
        print('6.hætta ')
        print('.......................')
        val=int(input('hver lið velðu ?'))

        if val == 1:
            fyrsta_tuple1 = ('hæ', 7.7, 'sæll', 7,  8.8, 8,)
            print('stak nr.3 er:',fyrsta_tuple1[3])
            for x in fyrsta_tuple1:
                print(x, end=":")
            print()    
                   
        elif val == 2:
            Annan_tuple2 = ([2,'takk',4],[6,'sjaumst',8],[10,12,'bless!'],[14,'jájá',16])
            for x in Annan_tuple2:
               print(x, end=' ')
            for x in Annan_tuple2:
               print(Annan_tuple2[2][2])
               
        elif val == 3:
            þriðja_tuple3 = ('T','A','E','K','N','I','S','K','O','L','A','N','U','M')
            print(þriðja_tuple3[5])
            print(þriðja_tuple3[-5])
            print(þriðja_tuple3[2:9])

        elif val == 4:
            tuptala_tala5 = (1,2,3,4,5)
            nytt = []
            tuptala5 = int(input('sláðu inn tölu'))
            
            for i in (tuptala_tala5):
                result = tuptala5*i
                nytt.append(result)
            print(nytt)

        elif val == 5:
            tuple_a=('a','v','c','x','o','y','d')
            stafa = input('slaður inn lágstafa')
            if stafa in tuple_a:
                print('stafurinn', stafa)
            else:
                print('þessi stafa', er, 'ekki til')

   




