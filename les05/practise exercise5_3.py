infile = open('kaartnummers.txt', 'r')
regels = infile.readlines()
infile.close()
print('deze file telt {} regels' .format(len(regels)))
hoogste= 0
regelnummer = 0
for regel in regels:
    kaartinfo = regel.split(',')
    kaartnummer = eval(kaartinfo[0])
    if kaartnummer > hoogste:
        hoogste = kaartnummer
print(hoogste)

