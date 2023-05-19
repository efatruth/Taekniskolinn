# Livinus bassey felix
# 15.2.2017
# Æfingaverkefni í heiltöludeilingu eða modulo
# Notum // til að deila venjulega en % til að fá afgang af deilingu

# dæmi 1, tek inn gráður og skila heilum hringjum og gráðum
gradur = int(input('Hvað eru gráðurnar margar? '))
venjulegDeiling = gradur / 360
hringir = gradur // 360 # Hér nota ég heiltöludeilingu til að fá heila hringi
gradurEftir = gradur % 360 # hér nota modulo til að fá afgang af heilum hringjum
print('Þetta er ekki það sem ég vil fá: ' + str(venjulegDeiling) + ' hringir')
print('Heldur vil ég hafa þetta svona:')
print(gradur, 'gráður gera', hringir, 'hringi og', gradurEftir, 'gráður')

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
