import xmltodict
def processXML(filename):
    with open(filename) as myXMLFILE:
        filestring = myXMLFILE.read()
        xmldictionary = xmltodict.parse(filestring)
        return xmldictionary
artikelendict = processXML('artikelen.xml')
artikelen = artikelendict['artikelen']['artikel']
for artikel in artikelen:
    print('het product is {} met een prijs van {}.\nmet als productcode {} en er zijn er {} van op voorraad.\n'.format(artikel['naam'], artikel['prijs'], artikel['code'],artikel['voorraad']))
