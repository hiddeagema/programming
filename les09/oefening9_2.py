naam = input('wat is je naam: ')
uitvoerfile = open('oefening9_1.txt', 'w')
while naam != '':
    uitvoerfile.write(naam  + '\n')
    naam = input('wat is je naam: ')
uitvoerfile.close()

