lijst = [[0,156,0,0], [34,0,0,0],[23,123,0,34]]
aantalrijen = len(lijst)
aantalkolommen = len(lijst[0])


def pixels(x):
    teller = 0
    aantalrijen = len(lijst)
    aantalkolommen = len(lijst[0])
    for rij in range(aantalrijen):
        for kolom in range(aantalkolommen):
            if x[rij][kolom] > 0:
                teller = teller + 1
    return teller
print(pixels(lijst))



