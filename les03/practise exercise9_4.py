import csv

with open('producten.csv','w',newline='') as myCSVFILE:
    writer = csv.writer(myCSVFILE,delimiter = ';')
    writer.writerow(('artikelnummer','artikelcode','naam','voorraad','prijs'))
    while True:
        artikelnummer = input('voer het artikelnummer in: ')
        if artikelnummer == 'einde':
            break
        artikelcode = input('voer de artikelcode in: ')
        naam = input('voer de naam in: ')
        voorraad = input('voer de voorraad in: ')
        prijs = input('voer de prijs in: ')
        writer.writerow((artikelnummer,artikelcode,naam,voorraad,prijs))


