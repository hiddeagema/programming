import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y")
print(s)
naam = input('geef je naam: ')
infile = open('hardlopers.txt', 'a')
infile.write('{} {}'.format(s,naam))
infile.close()
