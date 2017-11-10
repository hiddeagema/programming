def toon_aantal_kluizen_vrij():
    infile = open('kluizen.txt','r')
    kluizendata = infile.readlines()
    infile.close()
    aantalkluizen = len(kluizendata)
    aantalvrij= 12-aantalkluizen
    print('er zijn {} kluizen vrij'.format(aantalvrij))
def nieuwe_kluis():
    infile = open('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()
    stringnummer = input('welk nummer wil je? ')
    for kluis in kluizendata:
        gegevensvan1kluis = kluis.split(';')
        stringkluisnummer = gegevensvan1kluis[0]
        if stringkluisnummer == stringnummer:
            print('kies een andere kluis')
            return
        else:
            code = input()
def kluis_openen():
    infile = open('kluizen.txt','r')
    kluizendata = infile.readlines()
    infile.close()
    stringnummer = input('geef een kluisnummer: ')
    code=input('wat is je code: ')
    gegevenscorrect = False
    for kluis in kluizendata:
        gegevensvan1kluis= kluis.split(';')
        stringnummer= gegevensvan1kluis[0]
kluiscode = gegevensvan1kluis[1].strip()
if stringnummer == stringkluisnummer and code == kluiscode:
    gegevenscorrect = True

if gegevenscorrect:
    print('kluis is geopend')
else:
    print('kluis of wachtwoord incorrect')

def nieuwe_kluis():
    print(1)
keuze = eval(input('geef een keuze: '))
if keuze == 1:
    toon_aantal_kluizen_vrij()
elif keuze ==2:
    nieuwe_kluis()
elif keuze==3:
    kluis_openen()
else:
    print('u heeft geen geldige optie gekozen')
