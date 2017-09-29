lengte = eval(input('Hoe lang ben je?: '))
gewicht = eval(input('Hoe zwaar ben je?: '))
BMI = gewicht/(lengte**2)
print(BMI)
if (BMI <= 18.5):
    print('je hebt ondergewicht')
elif (BMI > 18.5) and (BMI <= 25):
    print('je hebt een normaal gewicht')
else:
    print('overgewicht')
