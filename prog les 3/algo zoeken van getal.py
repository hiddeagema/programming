getallenrij = [2, 4, 6, 8, 10, 9, 7]
zoekgetal = eval(input('voer een getal in: '))
gevonden = False
for getal in getallenrij:
    if getal == zoekgetal:
        gevonden = True
if gevonden == True:
    print('het zoekgetal zit in de getallenrij.')
else:
    print('het zoekgetal zit niet in de getallenrij.')



