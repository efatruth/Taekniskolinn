'''
livinus felix bassey
26.9.2017
tuples
profum alls konar með dictionary
'''

my_dict = {'nafn': 'felix', 'aldur':60}
print(my_dict)
print(my_dict['nafn'])
print(my_dict['aldur'])
#print(my_dict['hæd']) #þetta ekki hægt keyerror

# að prenta út key og value pör línu fyrir línu
my_dict = {1: 'apple', 2: 'ball', 3: 'orange', 4: 'banana',}
for x in my_dict:
    print(x, "\t",my_dict[x])
#eða svona
for key, value in my_dict.items():
    print('%i -> %s' % (key,value)
#nu eda svona
for key, value in my_dict.items():
    print('%{0} er{1}' .format(key, value))
#það er hægt að breyta og bæta inn í dictionary
my_dict = {'nafn': 'felix', 'aldur':60}
my_dict = ['aldur']= 65
print(my_dict)
my_dict['heimilisfang'] = 'vesturberg 78'
print(my_dict)
