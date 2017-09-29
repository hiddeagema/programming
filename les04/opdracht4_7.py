def standaardprijs(km):
    kosten = 0
    if km > 50:
        #extrakm = km - 50
        kosten = 15 + 0.60 * km
    elif km <= 0:
        kosten = 0
    else:
        kosten =0.80*km
    return kosten

#print(standaardprijs(51))
def ritprijs(leeftijd,weekendrit, km):
    prijs = standaardprijs(km)
    if weekendrit == True:
        if leeftijd < 12 or leeftijd >= 65:
            prijs = prijs*0.65
        else:
            prijs = prijs*0.60
    else:
        if leeftijd < 12 or leeftijd >= 65:
            prijs = prijs*0.70
    return prijs

print(ritprijs(11,True,50))



