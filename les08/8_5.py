def diceprob(invoersom):
    aantalworpinv = 0
    aantalworp = 0
    while aantalworpinv < 100:
        aantalogen1 = random.randrange(1, 7)
        aantalogen2 = random.randrange(1, 7)
        som = aantalogen1 + aantalogen2
        if som == invoersom:
            aantalwordinv += 1
        aantalworp += 1
    print('het aantal benodige worpen is {}'.format(aantalworp))

somaantalogen = eval(input('hoe groot is de som: '))
diceprob(somaantalogen)






