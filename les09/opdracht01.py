tabel = [[4,7,2,5],[5,1,9,2],[8,3,6,6]]
aantalrijen = len(tabel)
aantalkolommen = len(tabel[0])
for rij in range(aantalrijen):
    for kolom in range(aantalkolommen):
        if tabel[rij][kolom] %2 == 0:
            print(tabel[rij][kolom], end = ' ')


