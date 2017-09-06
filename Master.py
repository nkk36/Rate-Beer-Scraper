"""
SCRIPT DESCRIPTION
 
"""
from GetLinks import GetLinks
from GetBreweryTable import GetBreweryTable
from GetBreweryBeerTable import GetBreweryBeerTable

#Get links of all state and city breweries
links = GetLinks("I can put anything here")

#Get brewery-level data from state/city
data = []
for j in range(0,1,1): #For now only grab from one state
    df = GetBreweryTable(links, j)
    data.append(df)

#Get table of beers for each brewery
df = []
df2 = []
for i in range(0,len(data),1):
    for j in range(0,len(data[i]["Link"])):
        df.append(GetBreweryBeerTable(data[i]["Link"][j]))
    df2.append(df)