studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0]]
def gemiddeldeperstudent(studentencijfers):
    for getal in range (len(studentencijfers)):
        totaal = 0
        for nummer in studentencijfers[getal]:
            totaal += nummer
            gemiddelde = totaal / len(studentencijfers[0])
        return gemiddelde

def gemiddeldevanallestudenten(studentencijfers):
    som = 0
    lengte = 0
    for number in range (len(studentencijfers)):
        for getallen in studentencijfers[number]:
            lengte += 1
            som += getallen
    totaalgemiddelde = som / lengte
    return (totaalgemiddelde)

print(gemiddeldeperstudent(studentencijfers))
print(gemiddeldevanallestudenten(studentencijfers))
