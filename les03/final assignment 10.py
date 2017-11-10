def import xmltodict
def processXML(filename):
    with open(filename) as myXMLFILE:
        filestring = myXMLFILE.read()
        xmldictionary = xmltodict.parse(filestring)
        return xmldictionary
stationsdict = processXML('FA10.xml')
stations = stationsdict['Stations']['Station']
code = station['code']
type = station['type']
synoniemen = station['Synoniemen']
for station in stations:
    if station['Synoniemen'] is not None:
        print('{:4} - {}'.format(station['Code'],station['Type'],station['Synoniemen']))

def import xmltodict
def processXML(filename):
    with open(filename) as myXMLFILE:
        filestring = myXMLFILE.read()
        xmldictionary = xmltodict.parse(filestring)
        return xmldictionary
stationsdict = processXML('FA10.xml')
stations = stationsdict['Stations']['Station']
code = station['code']
type = station['type']
synoniemen = station['Synoniemen']
for station in stations:
    print('{:4} - {}'.format(station['Code'],station['Type']))

import xmltodict
xmlfile = xmltodict.parse(open("xml_stationslijst.xml").read())
print("Dit zijn de codes en types van de 4 stations:")
for station in xmlfile['Stations']['Station']: print(station['Code'],"-",station['Type'])
    print("\nDit zijn alle stations met een of meer synoniemen:")
for station in xmlfile['Stations']['Station']:
    if station['Synoniemen'] != None and len(station['Synoniemen']['Synoniem']) > 1:
        print(station['Code'],"-",station['Synoniemen'])
        print("\nDit is de lange naam van elk station:")#
for station in xmlfile['Stations']['Station']:
    print(station['Code'],"-",station['Namen']['Lang'])
