import csv

with open('inloggers.csv', 'w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')

    while True:
        naam = input('wat is je naam?: ')
        if naam == 'einde':
            break
        voorletter = input('wat is je voorletter?: ')
        geboortedatum = input('wat is je gebruikersnaam?: ')
        email = input('wat is je e-mail?: ')
        writer.writerow((naam,voorletter,geboortedatum,email))
        break

