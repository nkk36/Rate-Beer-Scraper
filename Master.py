"""
SCRIPT DESCRIPTION
 
"""
from GetLinks import GetLinks
from GetBreweryTable import GetBreweryTable
from GetBreweryBeerLinks import GetBreweryBeerLinks
from GetBreweryBeerTable import GetBreweryBeerTable

#Get links of all state and city breweries
links = GetLinks("I can put anything here")

#Get brewery-level data from state/city
data = []
for j in range(0,1,1): #For now only grab from one state
    df = GetBreweryTable(links, j)
    data.append(df)

#Get number of beer reviews for each brewery
L = len(data)
NumBeer = []
for i in range(0,L,1):
    NumBeer.append(data[i]["NumBeer"])
    
#Get links to each brewery
BreweryBeerLinks = GetBreweryBeerLinks(links, 0)

#Get table of beers for each brewery
df2 = GetBreweryBeerTable(BreweryBeerLinks["link"][0], 46)
    

    
