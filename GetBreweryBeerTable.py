# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 20:11:50 2017

@author: NKallfa
"""

def GetBreweryBeerTable(links, numbeer):
    
    #Import packages
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import numpy as np
    import re

    #Get url and scrape data
    url = "https://www.ratebeer.com/brewers/avondale-brewing-company/12890/"#links#["links"][j]
    page = requests.get(url, verify = False)
    soup = BeautifulSoup(page.text, "lxml")
    
    #Get table in numpy array
    array_df = []
    for rows in soup.find_all("td"):
        array_df.append(rows.text)
        
    aliasRegex = re.compile(r"(alias)")    
    delete = []
    L = len(array_df)
    for i in range(0, L, 1):
        if aliasRegex.search(array_df[i]) is not None:
            delete.append(i)
        else:
            pass
    
    deletearray = []
    index = 0
    for element in delete:
        deletearray.append(range(delete[index], element + 8,1))
        index += 1
        
    array_df = np.delete(array_df, deletearray)
        
    numactive = numbeer - len(delete)
    
    df = pd.DataFrame(np.reshape(array_df[:numactive*7],(numactive,7)), columns = ["Beer", "ABV", "DateAdded", "Rate", "Score", "Style", "NumRating"])
#    split_brewery_city = df["Brewery"].apply(lambda x: x.split("-"))
#    df_sbc = pd.DataFrame(np.concatenate(split_brewery_city, axis = 0).reshape(numactive,2), columns = ["Brewery","City"])
#    df["Brewery"] = df_sbc["Brewery"]
#    df.insert(1, "City", df_sbc["City"])
#    state = ["Alabama"]*numactive
#    df_state = pd.DataFrame(state, columns = ["State"])
#    df.insert(2, "State", df_state)
    
    return(df)
    
#    #Get number of breweries
#    numRegex = re.compile(r"\d{1,4}")
#    numactive = int(numRegex.search(soup.find_all("a", href = "#active")[0].text).group())
#    
#    BreweryLinks = soup.find_all("a", href = True)
#    
#    linkRegex = re.compile(r"/brewers/([\D])+(/)([0-9])+")
#     
#    links = []
#    for link in BreweryLinks:
#        if linkRegex.search(str(link)) is not None:
#            links.append(linkRegex.search(str(link)).group())
#        else:
#            pass
#    
#    tlinks = []
#    for i in range(0,numactive,1):
#        tlinks.append("https://www.ratebeer.com/" + links[i])
#    
#    tlinks = pd.DataFrame(tlinks, columns = ["links"])
#    return(tlinks)
#        