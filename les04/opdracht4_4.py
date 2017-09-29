klinker= 'aeiouAEIOU'
woord = input('geef een woord: ')
aantal = 0
for letter in woord:
    if letter in klinker:
        aantal = aantal + 1
print(aantal)
