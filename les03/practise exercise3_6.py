s = "Guido van Rossum heeft programmeertaal Python bedacht."
klinker = 'aeiou'
for woord in s:
    for letter in woord:
        if letter in klinker:
            print(letter)

