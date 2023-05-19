'''
livinus felix bassey
26.9.2017
tuples
'''

'''
my_tuple1 = ()
print(my_tuple1)
my_tuple2 = (1, 2, 3)
print(my_tuple2)
my_tuple3 = (1,'Halló', 3.4)
print(my_tuple3)
my_tuple4 = ('mus', [8,4,6], (1, 2, 3))
print(my_tuple4)
# það er hægt að ítra í gegnum tuplu eins og lista með for lukkju
for stak in my_tuple3:
    print(stak, end=' ')

print('\nþetta er innihaldið í my_tuple3')


my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple[0])
print(my_tuple[5])
# print(my_tuple[10]) ekki hægt ve3gna þess að tuplan er oft stutt
for stak in my_tuple:
    print(stak, end=' ')
print()
for i range(len(my_tuple)):
    print(my_tuple[i], end=' ')
'''
# Hreyðraðar tuplur eða nested tuple
n_tuple = ('mus', [8, 4, 6], (1, 2, 3))
print(n_tuple[0][1], n_tuple[0][2])
for i in range(len(n_tuple)):
    for n in range(len(n_tuple[1])):
        print(n_tuple[i][n], end=' ')
    print()
for holf in my_tuple:
    for staf í holf:
        for in my_tuple:
