"""
SCRIPT DESCRIPTION
 
"""
import pandas as pd
from GetLinks import GetLinks
from GetBreweryTable import GetBreweryTable
from GetBreweryBeerTable import GetBreweryBeerTable
from GetBeerReviews import GetBeerReviews

##Get links of all state and city breweries
#links = GetLinks("I can put anything here")
#
##Get brewery-level data from state/city
#data = []
#for j in range(0,len(links),1): 
#    df = GetBreweryTable(links, j)
#    data.append(df)
#
##Get table of beers for each brewery
#df = []
#for i in range(0,len(data),1):
#    for j in range(0,len(data[i]["Link"])):
#        if data[i]["Brewery"][j] == "Phoenix Ale Brewery":
#            pass
#        else:
#            df.append(GetBreweryBeerTable(data[i]["Link"][j], data[i]["Brewery"][j], data[i]["City"][j], data[i]["State"][j]))

LocalBeers = pd.read_csv("LocalBeers.csv", encoding = "latin-1")

df3 = pd.DataFrame()

for i in range(2787, len(testlocal)):
    row = GetBeerReviews(testlocal["Link"][i], testlocal["Beer"][i], testlocal["Brewery"][i], testlocal["City"][i], testlocal["State"][i])
    if isinstance(row, pd.DataFrame):
        df3 = df3.append(row)
    
    
    
    
    