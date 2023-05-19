'''
livinus
'''
#æfinga

texti = input('sláðu inn texta ')
skra = open("skra.txt", "w", encoding="utf-8")
skra.write(texti)
skra.close()

skra = open("skra.txt", "r", encoding="utf-8")
print (skra.read())
skra.close()

#æfinga B
skra = open("skra.txt", "w", encoding="utf-8")
