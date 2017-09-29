string = eval(input('voer een string in: '))
for karakter in string:
    asc = ord(karakter)
    print('de ascii waarde is {}' .format(asc) , 'de binaire waarde is {:b}' .format(asc) , 'de hexadecimale waarde is {:x}' .format(asc))
    print('{} {} {:b} {:x}' .format(karakter, asc,asc,asc))
