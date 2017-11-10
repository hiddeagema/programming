cursus = {'bas':8.1, 'kees':9.2, 'kareltje':6.2, 'achmed':7.3, 'max':9.3, 'piet':3.3, 'manon':9.1, 'emma':9.7}
for naam in cursus:
    if cursus[naam] >9.0:
        print('{} heeft een {} gehaald'.format(naam,cursus[naam]))
