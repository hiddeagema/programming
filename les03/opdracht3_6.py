lst = ['Henk', 'Pieter', 'Emil', 'Iris', 'Levi', 'Hidde', 'Janet']
naam = input('Voer een naam in: ')
if naam in lst:
    print('Naam ' + naam + ' komt voor in de lijst')
else:
    print('Naam ' + naam+ ' komt niet voor in de lijst')
