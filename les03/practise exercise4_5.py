def kwadraten_som(grondgetallen):
    som = 0
    for i in grondgetallen:
        if i > 0:
            som = som + i**2
    return som

lijst = [4,5,3,-81]
print(kwadraten_som(lijst))
