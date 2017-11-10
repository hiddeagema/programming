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
            code = input('kies uw code: ')
            herhalingcode = input('herhaal uw code: ')
            if code != herhalingcode:
                infile = open('kluizen', 'w')
                infile.append(stringkluisnummer + ': ' + code)
                infile.close()
                print('uw codes komen niet overeen')
                return
            else:
                print('uw codes komen overeen')
                return

def kluis_openen():
    infile = open('kluizen.txt','r')
    kluizendata = infile.readlines()
    infile.close()
    stringnummer = input('geef een kluisnummer: ')
    code=input('wat is je code: ')
    gegevenscorrect = False
    for kluis in kluizendata:
        gegevensvan1kluis= kluis.split(';')
        stringkluisnummer= gegevensvan1kluis[0]
        kluiscode = gegevensvan1kluis[1].strip()
        if stringkluisnummer == stringkluisnummer and kluiscode == code:
            gegevenscorrect = True
    if gegevenscorrect:
        print('kluis is geopend')
    else:
        print('kluis of wachtwoord incorrect, de kluis wordt niet geopend')
print('1: ik wil weten hoeveel kluizen er nog vrij zijn')
print('2: ik wil een nieuwe kluis')
print('3: ik wil even iets uit mijn kluis halen')
keuze = eval(input('voer uw keuze in: '))
if keuze ==1:
    toon_aantal_kluizen_vrij()
elif keuze ==2:
    nieuwe_kluis()
else:
    kluis_openen()

