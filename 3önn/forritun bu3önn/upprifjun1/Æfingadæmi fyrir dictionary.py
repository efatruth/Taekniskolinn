'''
livinus felix bassey
02.10.2017
Æfingadæmi fyrir dictionary
'''

key_liti = {1:'gulur', 2:'svartur', 3:'hvitur', 4:'rauður', 5:'appelsínugult', 6:'brúnn', 7:'grænn', 8:'blár', 9:'bleikur', 10:'fjólublátt'}#dictionaryið er hannið
for x in key_liti:
    print('númer', x, 'er', key_liti[x])# útskrift af dictionaryið
print(key_liti[4])
key_liti[5] = "appelsínugulur"
print(key_liti)
key_liti.pop(2)
print(key_liti)
key_liti.popitem()
print(key_liti)

anna_liti = key_liti
del key_liti
#print(key_liti)
#NameError: name 'key_liti' is not defined
#hlutur ekki til og ekki hægt að prenta það sem er ekki til

nytt_liti = {1:1, 2:4, 3:6, 4:8, 5:'value'}
print(nytt_liti)

print('.........')
nytt_liti.keys()
print(nytt_liti.keys())

print('............')
nytt_liti.items()
print(nytt_liti.items())

print('............')
nytt_liti.values()
print(nytt_liti.values())

print('............')
nytt_liti.clear()
print(nytt_liti.clear())


