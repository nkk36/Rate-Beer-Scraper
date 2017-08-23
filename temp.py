#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 15:11:47 2017

@author: nicholaskallfa
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = links["links"][0]
page = requests.get(url, verify = False)
soup = BeautifulSoup(page.text, "lxml")

brewT = soup.find_all('table', attrs = {"id": "brewerTable"})

df = pd.DataFrame(index = range(0,33,1), columns = ["Brewery", "Type", "NumBeer", "MyCount", "Est"])
####This works
#df2 = []
#for rows in soup.find_all("td"):
#    df2.append(rows.text)

#Get number of breweries
numactive = soup.find_all("a", href = "#active")
count = 0                    

for rows in soup.find_all("td"):
    if count > 33:
        break
    else:
        for i in range(0,5,1): 
            df[df.columns[i]][i] = rows.text
        count += 1

#Get headers
#soup.find_all("th")

#Get name of Breweries and city locations
#soup.find_all("a", href = True)

#Get only brewery city locations
#soup.find_all("a", {"class" : "filter"})