lijst= eval(input('geef een lijst van min. 10 woorden:' ))
if len(lijst) >= 10:
    for woord in lijst:
        if len(woord) == 4:
            print(woord)

