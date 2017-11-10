som = 0
aantal = 0
getal= eval(input('Geef een getal: '))
while getal !=0:
    som = som + getal
    aantal = aantal + 1
    getal = eval(input('Geef een getal: '))
print('Er zijn {} getallen in gevoerd en de som is {}'.format(aantal,som))
