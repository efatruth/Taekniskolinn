'''
livinus felix
lokaverkefni1
22.11.2017
'''

from random import *

class Nagdyr:
        def __init__(self,tegund,staðsetning, afi):
            self.tegund = tegund
            self.stadsetning = staðsetning
            self.afi = afi
        def __str__(self):
            return


from klasar.klasi1 import *

from klasar.klasi2 import *

nagdyrin = []
afl = [2,4,6]
nagdyrin.append(nagdyr("mus",1,afl[randint(0,2)]))
nagdyrin.append(nagdyr("hamstur",randint(2,100),afl[randint(0,2)]))
