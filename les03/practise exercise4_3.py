def lang_genoeg(lengte):
    if lengte > 1.20:
        return 'je mag in de achtbaan'
    else:
        return'sorry, je bent te klein'


lengte = eval(input('hoe lang ben je: '))

print(lang_genoeg(lengte))
