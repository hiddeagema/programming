try:
    bedrag = 4356
    aantal = eval(input('geef bedrag: '))
    if bedrag < 0:
        print('negatieve getallen niet printen')
    else:
        print(bedrag/aantal)
except ZeroDivisionError:
    print('delen door 0 kan niet')
except NameError:
    print('gebruik cijfers')
except:
    print('onjuiste invoer')
