tabel = [[4,7,8,9], [1,8,3,6], [9,1,1,5]]
for rij in range(len(tabel)):
    for kolom in range(len(tabel[0])):
        print(tabel[rij][kolom], end = ' ')
    print()


for i in range(len(tabel)):
    print(tabel[i][1])
