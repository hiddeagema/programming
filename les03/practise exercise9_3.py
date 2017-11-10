import csv
with open('gamers.csv', 'r') as myCSVFile:
    reader= csv.reader(myCSVFile, delimiter=';')
    maxscore = 0
    maxdatum = 0
    for row in reader:
        score = int(row[2])
        if score > maxscore:
            maxscore = score
            maxnaam = row[0]
            maxdatum = row[1]
    print('de hoogste score was {} van {} op {}.format'(maxscore,maxnaam,maxdatum))

