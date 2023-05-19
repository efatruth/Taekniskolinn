'''
livinus felix bassey
07.03.18
FORR2FA05BU - SKRÁRVINNSLA_Skilaverkefni_4
'''

with open("slettartolur.txt", 'w', encoding='utf-8') as f:
    for stak in range(2, 1001):
        if stak % 2 == 0:
            f.write(str(stak) + ' ')

listir = []
with open("slettartolur.txt", 'r', encoding='utf-8') as f:
    for line in f:
        print(line)

listir = []
with open("slettartolur.txt", 'r', encoding='utf-8') as f:
    line = f.read()
    line.strip()
    listir = (line.split(' '))
listir.remove('')
listir = list(map(int, listir))

print("summa", sum(listir))
print("medaltal", round(sum(listir) / len(listir), 2))
print("medaltal", format(sum(listir) / len(listir), ".2f"))

listir2 = []
for prime in range(2, 101):
    er_prime = True
    for items in range(2, prime):
        if prime % items == 0:
            er_prime = False
            break
    if er_prime == True:
        listir2.append(prime)

print(listir2)
# að setja inni skrá
with open("primtolur.txt", 'w', encoding='utf-8') as f:
    for item in listir2:
        f.write(str(item) + ' ')

with open("primtolur.txt", 'r', encoding='utf-8') as f:
    print(f.read())

listir3 = []

# númer3
'''
tuple_1 = (1,2,3,4,5,6,7,8,9)

tuple_2 = ('a','b','c','d','e','f','g','h')

tuple_3 = ('konni',1234,'sæll','blessaður',2468)

with open("þrja_tuple.txt",'w',encoding = 'utf-8') as f:
    f.write('(')
    for item in tuple_1:
        f.write(str(item) + ',')
    f.write(')\n(')
    for item in tuple_2:
        f.write(str(item) + ',')
    f.write(')\n(')
    for item in tuple_3:
        f.write(str(item) + ',')
    f.write(')')
'''
with open("þrja_tuple.txt", 'r', encoding='utf-8') as f:
    for line in f:
        print(line)
    f.seek(0)
    tuple_text = f.readline()
summa = 0
for c in tuple_text:
    if c.isdigit():
        summa = summa + int(c)
print(summa)

# print("summa",sum(new_tuple))

# númer4

# skra_dict = {'kalli':1, 'konni':2, 'takk':3, 'sjáumst':4}
skra_dict1 = {'Jón': 2, 'Krístinn': 4, 'Páll': 6, 'Ólafur': 8}
skra_dict2 = {'james': 5, 'kiki': 6, 'reuben': 7, 'aron': 9}

with open("geymir_dict.txt", 'r', encoding='utf-8') as f:
    print(f.read())

with open("geymir_dict.txt", "a", encoding='utf-8') as f:
    f.write('\n' + str(skra_dict1) + '\n' + str(skra_dict2))
# di1 = {}
# di2 = {}
# di3 = {}
with open("geymir_dict.txt", 'r', encoding='utf-8') as f:
    f.seek(0)
    # texti = f.readline()
    # di1 = eval(texti)



