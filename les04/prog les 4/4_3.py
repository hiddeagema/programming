def swap (lijst):
   if len(lijst) >1:
       lijst[0] , lijst[1] = lijst[1] , lijst[0]
       return(lijst)

lijst = [4,0,1,-2]
nieuw = swap(lijst)
print(nieuw)
