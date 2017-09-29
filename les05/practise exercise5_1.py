def convert(celsius):
    fahrenheit = celsius *1.8 + 32
    return fahrenheit


def table():
    print('\t{:8} {:8} ' .format('c','f'))
    for i in range(-30, 41, 10):
        print('{:8} {:8} ' .format(i,convert(i)))
table()


