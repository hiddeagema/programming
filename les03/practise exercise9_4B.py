import csv
with open('producten.csv', 'r') as myCSVFILE:
    reader = csv.DictReader(myCSVFILE,delimiter=';')
    maxprijs = 0
    for row in reader:
        prijs = float(row['prijs'])
        if prijs > maxprijs:
            maxprijs = prijs
            maxnaam= row['naam']
            voorraad = row['voorraad']
            artikelnummer = row['artikelnummer']
    print('het duurste product is {} met als prijs {}het kleinste aantal voorraad is {} met als artikelnummer {}.format'(maxnaam,maxprijs,voorraad,artikelnummer))
