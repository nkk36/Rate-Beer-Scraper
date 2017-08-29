# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 21:18:12 2017

@author: NKallfa
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

"""
Problem I am having: I can grab the beers from each brewery, but I am having trouble getting a data frame because alias beers appear
that give extra spaces in the brewery-beer table
"""

L = len(data)
NumBeer = []
for i in range(0,L,1):
    NumBeer.append(data[i]["NumBeer"])
    

BreweryBeerLinks = GetBreweryBeerLinks(links, 0)

df2 = GetBreweryBeerTable(BreweryBeerLinks["link"][0], 46)
    
    
