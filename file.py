import csv
import plotly.express as pl

rows = []

with open('anyname.csv', 'r') as f:
    reader = csv.reader(f)
    

    for i in reader:
        rows.append(i)

headers = rows[0]
planetInfo = rows[1:]

headers[0] = 'index'

planetCount = {}

for i in planetInfo:
    if planetCount.get(i[11]):
        planetCount[i[11]] += 1
    else:
        planetCount[i[11]] = 1

maxSolarSystem = max(planetCount, key=planetCount.get)



planetsInSolar = list(planetInfo)



for i in planetsInSolar:
    planetMass = i[3]
    planetRadius = i[7]
    
    if planetMass.lower() == 'unknown':
        planetInfo.remove(i)
        continue
    else:
        planetMassValue = planetMass.split(' ')[0]
        planetMassRef = planetMass.split(' ')[1]
        
        if planetMassRef == 'Jupiters' or planetMassRef == 'Jupiter':
            planetMassValue = float(planetMassValue) * 317.8
            
        i[3] = planetMassValue

    if planetRadius.lower() == 'unknown':
        planetInfo.remove(i)
        continue
    else:
        planetRadiusValue = planetRadius.split(' ')[0]
        planetRadiusRef = planetRadius.split(' ')[2]
        
        if planetRadiusRef == 'Jupiter' or planetRadiusRef == 'Jupiters':
            planetRadiusValue = float(planetRadiusValue) * 11.2
            
        i[7] = planetRadiusValue

planets = []
massOfPlanets = []
nameOfPlanets = []
radiusOfPlanets = []
gravityOfPlanets = {}
for i in planetsInSolar:
    if maxSolarSystem == i[11]:
        planets.append(i)
for i in planetInfo:
    massOfPlanets.append(i[3])
    radiusOfPlanets.append(i[7])
    nameOfPlanets.append(i[1])

gravityOfPlanets['name'] = []
gravityOfPlanets['gravity'] = []
gravity = []
for i, v in enumerate(nameOfPlanets):
    G = 6.674e-11
    Gravity = (G * float(massOfPlanets[i]) * 5.972e+24)/((float(radiusOfPlanets[i]) * 6371000) * (float(radiusOfPlanets[i]) * 6371000))     
    gravityOfPlanets['name'].append(v)
    gravityOfPlanets['gravity'].append(Gravity)
    gravity.append(Gravity)
#graph = pl.scatter(x = radiusOfPlanets, y = massOfPlanets, size = gravityOfPlanets)
#graph.show()

gravitys = gravityOfPlanets['gravity']
names = gravityOfPlanets['name']
goodPlanets = []

for i, v in enumerate(gravity):
    if v < 100:
        goodPlanets.append(planetInfo[i])

print(len(goodPlanets))

types = []

for v in planetInfo:
    types.append(v[6])

print(set(types))

MOGP = []
ROGP = []

for v in planetInfo:
    MOGP.append(v[3])
    ROGP.append(v[7])

'''
graph = pl.scatter(x = ROGP, y = MOGP, color = types)
graph.show()
'''   



betterPlanets = []
for v in goodPlanets:

    if v[6] == 'Super Earth' or v[6] == 'Terrestrial':
        betterPlanets.append(v)
    

for i in betterPlanets:
    if i[8].lower() == 'unknown':
        betterPlanets.remove(i)
for v in betterPlanets:
    if v[9].split(' ')[1].lower() == 'days':
        v[9] = float(v[9].split(' ')[0])
    else:
        v[9] = float(v[9].split(' ')[0]) * 365
           





       
    