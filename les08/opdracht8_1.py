naam = input('wat is je naam: ')
woonplaats = input('waar woon je: ')
outfile = open('opdracht81.txt','w')
outfile.write('mijn naam is ' + naam + '\n')
outfile.write('mijn woonplaats is ' + woonplaats + '\n')
outfile.close()



